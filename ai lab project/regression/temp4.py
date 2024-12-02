import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Load the data
data = pd.read_csv('data.csv')  # Replace with your dataset path

# Preprocessing
sim_dummies = data['No_of_sim'].str.strip().str.get_dummies(sep=',').add_prefix('Sim_')
data = data.drop('No_of_sim', axis=1).join(sim_dummies)
data = data[data['Battery'].str.contains('mAh Battery')]
data['Battery'] = data['Battery'].str.rstrip(' mAh Battery ').astype(int)
data = data[data['Ram'].str.contains('GB RAM')]
data['Ram'] = data['Ram'].str.rstrip(' GB RAM ').astype(float)
data['Display'] = data['Display'].str.strip(' inches ').astype(float)
data.drop('External_Memory', axis=1, inplace=True)
data['Android_version'] = data['Android_version'].str.replace(r"\(.*?\)", "", regex=True)
data['Android_version'] = data['Android_version'].astype(float)
data['Price'] = data['Price'].str.replace(',', '').astype(int)
data['Inbuilt_memory_GB'] = data['Inbuilt_memory'].str.replace('1 TB inbuilt', '1000').str.replace('GB inbuilt', '').astype(int)
data.drop('Inbuilt_memory', axis=1, inplace=True)
data = data.dropna()

# Encode categorical data
encoder = LabelEncoder()
for col in data.select_dtypes(include=['object']).columns:
    data[col] = encoder.fit_transform(data[col])

# Feature selection
correlation = data.corr()
FEATURES = correlation['Price'].abs().sort_values(ascending=False).drop('Price').head(10).index
X = data[FEATURES]
y = data['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Models to test
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor(),
    "Gradient Boosting": GradientBoostingRegressor(),
    "Extra Trees": ExtraTreesRegressor(),
    "Support Vector Machine": SVR(kernel='rbf')
}

# Train and evaluate models
results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = r2_score(y_test, y_pred) * 100
    mse = mean_squared_error(y_test, y_pred)
    results.append((name, accuracy, mse))

# Display results
results_df = pd.DataFrame(results, columns=['Model', 'R2_Score (%)', 'MSE'])
print(results_df)

# Visualize results
plt.figure(figsize=(10, 6))
sns.barplot(data=results_df.sort_values(by='R2_Score (%)', ascending=False), x='R2_Score (%)', y='Model')
plt.title('Model Accuracy Comparison')
plt.show()
