import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load datasets
iris = load_iris()
california_housing = fetch_california_housing()

# Display dataset information
print("Iris feature names:", iris.feature_names)
print("Iris data:\n", iris.data)
print("Iris target names:", iris.target_names)
print("Iris target:", iris.target)

print("California housing feature names:", california_housing.feature_names)
print("California housing data:\n", california_housing.data)
print("California housing target:", california_housing.target)

# Create DataFrames
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
california_housing_df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)

# Check for missing values
print("Missing values in Iris dataset:\n", iris_df.isnull().sum())
print("Missing values in California housing dataset:\n", california_housing_df.isnull().sum())

# Scale the data
scaler = StandardScaler()
iris_df_scaled = scaler.fit_transform(iris_df)
iris_df_scaled = pd.DataFrame(data=iris_df_scaled, columns=iris.feature_names)

california_housing_df_scaled = scaler.fit_transform(california_housing_df)
california_housing_df_scaled = pd.DataFrame(data=california_housing_df_scaled, columns=california_housing.feature_names)

# Train-test split for Iris dataset
X_train, X_test, y_train, y_test = train_test_split(iris_df_scaled, iris.target, test_size=0.2, random_state=42)

# Display test and train data
print("X test:\n", X_test.head())
print("X train:\n", X_train.head())

# Plotting
plt.figure(figsize=(12, 5))

# Scatter plot for Iris dataset
plt.subplot(1, 2, 1)
plt.scatter(X_train['sepal length (cm)'], X_train['sepal width (cm)'], c=y_train, cmap='viridis')
plt.title('Iris Dataset: Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.colorbar(label='Target Class')

# Scatter plot for California Housing
plt.subplot(1, 2, 2)
plt.scatter(california_housing_df['MedInc'], california_housing.target, alpha=0.5)
plt.title('California Housing: Median Income vs Target')
plt.xlabel('Median Income')
plt.ylabel('House Value')
plt.show()
