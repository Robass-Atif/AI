import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor, VotingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Load the data
data = pd.read_csv('data.csv')
print("Initial Data Preview:")
print(data.head())

# Check for missing values and duplicates
print("\nMissing Value Percentage:")
print((data.isna().sum() / len(data) * 100).round(2).sort_values(ascending=False))
print(f"Duplicated rows: {data.duplicated().sum()}")

# Data Cleaning and Feature Engineering
print("\nProcessing data...")
# One-hot encode 'No_of_sim' and drop the original column
sim_dummies = data['No_of_sim'].str.strip().str.get_dummies(sep=',').add_prefix('Sim_')
data = data.drop('No_of_sim', axis=1).join(sim_dummies)

# Clean and convert numeric columns
data = data[data['Battery'].str.contains('mAh Battery')]
data['Battery'] = data['Battery'].str.rstrip(' mAh Battery ').astype(int)

data = data[data['Ram'].str.contains('GB RAM')]
data['Ram'] = data['Ram'].str.rstrip(' GB RAM ').astype(float)

data['Display'] = data['Display'].str.strip(' inches ').astype(float)
data.drop('External_Memory', axis=1, inplace=True)

data['Android_version'] = data['Android_version'].str.replace(r"\(.*?\)", "", regex=True)
data['Android_version'] = data['Android_version'].str.replace('7.1.1', '7.1').astype(float)

data['Price'] = data['Price'].str.replace(',', '').astype(int)

# Standardize company names
data['company'] = data['company'].replace({
    'iQOO': 'IQOO', 'Oppo': 'OPPO', 'Poco': 'POCO', 'Itel': 'ITEL', 'itel': 'ITEL'
})

# Clean and convert inbuilt memory
data['Inbuilt_memory_GB'] = data['Inbuilt_memory'].str.replace('1 TB inbuilt', '1000') \
    .str.replace('GB inbuilt', '').astype(int)
data.drop('Inbuilt_memory', axis=1, inplace=True)

# Extract fast charging numeric data
data['fast_charging'] = data['fast_charging'].str.replace(r'\D', '', regex=True).replace('', np.nan).astype(float)

# Drop unnecessary columns
data.drop(columns=['Screen_resolution', 'Camera', 'Name'], inplace=True)

# Process processor data
data['Processor'] = data['Processor'].str.strip().replace({
    'Nine-Cores': 'Nine Cores', 'Nine Core': 'Nine Cores', 'Nine Coress': 'Nine Cores'
})
data['Processor_name_manufacturer'] = data['Processor_name'].str.split(' ', expand=True)[0]
data.drop('Processor_name', axis=1, inplace=True)

# Drop rows with missing values
data = data.dropna()




# Visualization: Company Market Share
plt.figure(figsize=(8, 8))
company_distribution = data['company'].value_counts()
# show only top 5 companies
company_distribution = company_distribution.head(5)

company_distribution.plot.pie(autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Market Share by Company', fontsize=16)
plt.ylabel('')  # Remove default ylabel
plt.tight_layout()
plt.show()

# Prepare Features and Target Variable
X = data.drop('Price', axis=1)
y = data['Price']

# One-hot encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Standardize features
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Hyperparameter Tuning for ExtraTreesRegressor
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

print("\nPerforming Grid Search...")
grid_search = GridSearchCV(ExtraTreesRegressor(random_state=0), param_grid, cv=5, n_jobs=-1, scoring='r2')
grid_search.fit(X_train_scaled, y_train)

# Best model
best_extr = grid_search.best_estimator_
print(f"Best parameters: {grid_search.best_params_}")

# Ensemble Model using Voting Regressor
voting_regressor = VotingRegressor(estimators=[
    ('extra_trees', best_extr),
    ('random_forest', RandomForestRegressor(random_state=0)),
    ('gradient_boosting', GradientBoostingRegressor(random_state=0))
])

print("\nTraining Voting Regressor...")
voting_regressor.fit(X_train_scaled, y_train)

# Model Evaluation
y_pred = voting_regressor.predict(X_test_scaled)
accuracy = voting_regressor.score(X_test_scaled, y_test) * 100
print("\nEvaluation Results:")
print(f"Ensemble Model Accuracy: {np.round(accuracy, 2)}%")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

# Cross-Validation Score
cv_scores = cross_val_score(voting_regressor, X, y, cv=10, scoring='r2')
print(f"Cross-validated R2 score: {np.mean(cv_scores) * 100:.2f}%")
