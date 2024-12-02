import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Load the data
data = pd.read_csv('data.csv')  # Load the dataset from CSV

# Process 'No_of_sim' column by converting to dummy variables
sim_dummies = data['No_of_sim'].str.strip().str.get_dummies(sep=',').add_prefix('Sim_')
data = data.drop('No_of_sim', axis=1).join(sim_dummies)

# Prepare 'Battery' column (convert text to integer)
data = data[data['Battery'].str.contains('mAh Battery')]
data['Battery'] = data['Battery'].str.rstrip(' mAh Battery ').astype(int)

# Prepare 'Ram' column (convert text to float)
data = data[data['Ram'].str.contains('GB RAM')]
data['Ram'] = data['Ram'].str.rstrip(' GB RAM ').astype(float)

# Prepare 'Display' column (convert text to float)
data['Display'] = data['Display'].str.strip(' inches ').astype(float)

# Drop unnecessary column 'External_Memory'
data.drop('External_Memory', axis=1, inplace=True)

# Clean and convert 'Android_version' column to float
data['Android_version'] = data['Android_version'].str.replace(r"\(.*?\)", "", regex=True)
data['Android_version'] = data['Android_version'].str.replace('7.1.1', '7.1')
data['Android_version'] = data['Android_version'].astype(float)

# Prepare 'Price' column by removing commas and converting to integer
data['Price'] = data['Price'].str.replace(',', '').astype(int)

# Standardize company names in 'company' column
data['company'] = data['company'].str.replace('iQOO', 'IQOO').str.replace('Oppo', 'OPPO').str.replace('Poco', 'POCO').str.replace('Itel', 'ITEL').str.replace('itel', 'ITEL')

# Convert 'Inbuilt_memory' to integer and drop the original column
data['Inbuilt_memory_GB'] = data['Inbuilt_memory'].str.replace('1 TB inbuilt', '1000').str.replace('GB inbuilt', '').astype(int)
data.drop('Inbuilt_memory', axis=1, inplace=True)

# Clean 'fast_charging' column
data['fast_charging'] = data['fast_charging'].str.replace(r'\D', '', regex=True)
data['fast_charging'] = data['fast_charging'].replace('', np.nan).astype(float)

# Drop irrelevant or redundant columns
data.drop(columns=['Screen_resolution', 'Camera', 'Name'], inplace=True)

# Clean and process 'Processor' and extract manufacturer
data['Processor'] = data['Processor'].str.strip().str.replace('Processor', '').str.replace('Nine-Cores', 'Nine Cores').str.replace('Nine Core', 'Nine Cores').str.replace('Nine Coress', 'Nine Cores')
data['Processor_name_manufacturer'] = data['Processor_name'].str.split(' ', expand=True)[0]
data.drop('Processor_name', axis=1, inplace=True)

# Drop remaining rows with missing values
data = data.dropna()

# Encode categorical columns
encoder = LabelEncoder()
o_cols = data.describe(include='object').columns

for column in o_cols:
    data[column] = encoder.fit_transform(data[column])

# Calculate correlations and select top 10 features most correlated with 'Price'
corr = data.corr()
FEATURES = corr['Price'].round(2).abs().sort_values(ascending=False).drop('Price', axis=0)[:10].index
TARGET = 'Price'

# Split data into features (X) and target (y)
X = data[FEATURES]
y = data[TARGET]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train an ExtraTreesRegressor model
extr = ExtraTreesRegressor(random_state=0).fit(X_train, y_train)

# Calculate accuracy on training and test data
train_accuracy = extr.score(X_train, y_train) * 100
test_accuracy = extr.score(X_test, y_test) * 100

print("Accuracy on training data: ", np.round(train_accuracy, 2), "%")
print("Accuracy on test data: ", np.round(test_accuracy, 2), "%")

# Hyperparameter tuning for ExtraTreesRegressor
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=ExtraTreesRegressor(random_state=0), param_grid=param_grid, cv=3, scoring='r2', n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Best parameters and score
best_params = grid_search.best_params_
best_score = grid_search.best_score_
print(f"Best parameters: {best_params}")
print(f"Best cross-validation score: {np.round(best_score * 100, 2)}%")

# Train a model with the best parameters
optimized_model = ExtraTreesRegressor(**best_params, random_state=0)
optimized_model.fit(X_train, y_train)

# Calculate accuracy on the training and test data using the optimized model
train_accuracy_optimized = optimized_model.score(X_train, y_train) * 100
test_accuracy_optimized = optimized_model.score(X_test, y_test) * 100

print("Optimized model accuracy on training data: ", np.round(train_accuracy_optimized, 2), "%")
print("Optimized model accuracy on test data: ", np.round(test_accuracy_optimized, 2), "%")
