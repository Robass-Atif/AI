import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Load the data
data = pd.read_csv('data.csv')  # Load the dataset from CSV
print(data.head())  # Preview the first few rows of the dataset

# Check for missing values and duplicates
(data.isna().sum() / len(data) * 100).round(2).sort_values(ascending=False)
data.duplicated().sum()

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

# Visualize data distribution with boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(data)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Encode categorical columns
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
o_cols = data.describe(include='object').columns

sub = data.copy()
for column in o_cols:
    sub[column] = encoder.fit_transform(sub[column])

# Calculate correlations and select top 10 features most correlated with 'Price'
corr = sub.corr()
FEATURES = corr['Price'].round(2).abs().sort_values(ascending=False).drop('Price', axis=0)[:10].index
TARGET = 'Price'

# Split data into features (X) and target (y)
X = sub[FEATURES]
y = sub[TARGET]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Print dataset shapes
print(f'X_train shape: {X_train.shape}')
print(f'y_train shape: {y_train.shape}')
print(f'X_test shape: {X_test.shape}')
print(f'y_test shape: {y_test.shape}')

# Train an ExtraTreesRegressor model
from sklearn.ensemble import ExtraTreesRegressor
extr = ExtraTreesRegressor().fit(X_train, y_train)

# Calculate and print accuracy
accuracy = extr.score(X_test, y_test) * 100
print("Accuracy of the model is: ", np.round(accuracy, 2), "%")

# Predict on the test set
y_pred = extr.predict(X_test)

# Create a DataFrame to compare actual vs predicted values
check = pd.DataFrame({'y_test': y_test, 'y_pred': y_pred})

# Visualize model predictions
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Scatterplot
sns.scatterplot(x='y_test', y='y_pred', data=check, ax=axes[0])
axes[0].set_title('Scatterplot')

# Histogram
sns.histplot(check, kde=True, ax=axes[1])
axes[1].set_title('Histplot')

# Boxplot
sns.boxplot(data=check, ax=axes[2])
axes[2].set_title('Boxplot')

plt.tight_layout()
plt.show()
