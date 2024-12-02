import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Load the data
data = pd.read_csv('data.csv')  # Load the dataset from CSV
print(data.head())  # Preview the first few rows of the dataset

# 1. Missing Values Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title("Missing Values Heatmap Before Preprocessing")
plt.show()

# Check for missing values and duplicates
print((data.isna().sum() / len(data) * 100).round(2).sort_values(ascending=False))
print(f"Number of duplicate rows: {data.duplicated().sum()}")

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

# 2. Distribution of Numerical Features Before Preprocessing
plt.figure(figsize=(10, 5))
sns.histplot(data['Price'], kde=True, color='blue', label='Original Price Distribution')
plt.title("Distribution of Price Before Preprocessing")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Encode categorical columns
encoder = LabelEncoder()
categorical_columns = data.select_dtypes(include='object').columns
for column in categorical_columns:
    data[column] = encoder.fit_transform(data[column])

# Correlation Heatmap After Preprocessing
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title("Correlation Matrix After Preprocessing")
plt.show()

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
extr = ExtraTreesRegressor().fit(X_train, y_train)

# Calculate and print accuracy
accuracy = extr.score(X_test, y_test) * 100
print("Accuracy of the model is: ", np.round(accuracy, 2), "%")

# Feature Importance Visualization
importances = pd.Series(extr.feature_importances_, index=X_train.columns)
importances.sort_values(ascending=True).plot(kind='barh', figsize=(10, 6), color='skyblue')
plt.title("Feature Importance (ExtraTreesRegressor)")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.show()
y_pred = extr.predict(X_test)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='purple', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', linewidth=2)
plt.title("Actual vs Predicted Prices")
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()

