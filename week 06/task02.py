import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    'EmployeeID': np.random.randint(1000, 10000, 1500),
    'Age': np.random.randint(22, 60, 1500),
    'Years_of_Experience': np.random.randint(1, 41, 1500),
    'Gender': np.random.choice(['Male', 'Female'], 1500),
    'Performance_Rating': np.random.randint(1, 6, 1500)
})

print(data.head(15))

# Second task
print(data.isnull().sum())

# task03
data['Years_of_Experience'].fillna(data['Years_of_Experience'].mean(), inplace=True)

# Task 4
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Task 5
plt.boxplot(data['Years_of_Experience'])
plt.title("Boxplot of Years of Experience")
plt.show()

# Filter out outliers
data = data[data['Years_of_Experience'] <= 40]

# Task 6:
data['Scaled_Age'] = (data['Age'] - data['Age'].mean()) / data['Age'].std()
data['Scaled_Experience'] = (data['Years_of_Experience'] - data['Years_of_Experience'].mean()) / data['Years_of_Experience'].std()

# Task 7
plt.boxplot(data['Performance_Rating'])
plt.title("Boxplot of Performance Rating")
plt.show()

# Scatter plot
plt.scatter(data['Years_of_Experience'], data['Performance_Rating'], alpha=0.5)
plt.xlabel("Years of Experience")
plt.ylabel("Performance Rating")
plt.title("Scatter Plot of Experience vs Performance")
plt.show()

# Correlation
correlation_matrix = data[['Age', 'Years_of_Experience', 'Performance_Rating']].corr()
print(correlation_matrix)

# Add feature
data['Experience_per_Age'] = data['Years_of_Experience'] / data['Age']

# Task 9
data.drop('EmployeeID', axis=1, inplace=True)

# Task 10
X = data.drop('Performance_Rating', axis=1)  
y = data['Performance_Rating']  

# task11
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining set size: {X_train.shape[0]}, Testing set size: {X_test.shape[0]}")
