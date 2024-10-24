# Task 4: Model Evaluation and Comparison
# Question 8: Evaluate Classification Models Using Classification Metrics
# - Use accuracy, precision, recall, and F1-score to evaluate the k-NN, SVM,
# and Random Forest models.
# Question 9: Evaluate Regression Models Using Regression Metrics
# - Compare the performance of Linear Regression and Decision Tree models
# using MSE and R² score.

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
iris = load_iris()
X = iris.data
y = iris.target
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f'k-NN Accuracy: {accuracy_knn:.2f}')
housing = fetch_california_housing()
X_housing = housing.data
y_housing = housing.target
X_train_housing, X_test_housing, y_train_housing, y_test_housing = train_test_split(X_housing, y_housing, test_size=0.3, random_state=42)
lr = LinearRegression()
lr.fit(X_train_housing, y_train_housing)
y_pred_lr = lr.predict(X_test_housing)
mse_lr = mean_squared_error(y_test_housing, y_pred_lr)
r2_lr = r2_score(y_test_housing, y_pred_lr)
print(f'Linear Regression MSE: {mse_lr:.2f}')
print(f'Linear Regression R²: {r2_lr:.2f}')
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train_housing, y_train_housing)
y_pred_dt = dt.predict(X_test_housing)
mse_dt = mean_squared_error(y_test_housing, y_pred_dt)
r2_dt = r2_score(y_test_housing, y_pred_dt)
print(f'Decision Tree MSE: {mse_dt:.2f}')
print(f'Decision Tree R²: {r2_dt:.2f}')