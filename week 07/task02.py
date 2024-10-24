from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
iris = load_iris()
scaler = StandardScaler()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df_scaled = scaler.fit_transform(iris_df)
X_train, X_test, y_train, y_test = train_test_split(iris_df_scaled, iris.target, test_size=0.2, random_state=42)
a = []
for k in range(1, 16):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    a.append(accuracy)
    print(f"Accuracy for k={k}: {accuracy:.4f}")
plt.plot(range(1, 16), a)
plt.title('KNN Classifier Accuracy for Different k Values')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.xticks(range(1, 16))
plt.grid(True)
plt.show()
kernels = ['linear', 'poly', 'rbf']
svm_accuracies = {}
for kernel in kernels:
    clf = svm.SVC(kernel=kernel)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    svm_accuracies[kernel] = accuracy
    print(f"Accuracy for SVM with {kernel} kernel: {accuracy:.4f}")

plt.bar(svm_accuracies.keys(), svm_accuracies.values())
plt.title('SVM Classifier Accuracy for Different Kernels')
plt.xlabel('Kernel')
plt.ylabel('Accuracy')
plt.show()

estimators = [1000, 50, 100]
rf_accuracies = {}
for n_estimators in estimators:
    rf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    rf_accuracies[n_estimators] = accuracy
    print(f"Accuracy for Random Forest with {n_estimators} estimators: {accuracy:.4f}")

plt.plot(estimators, list(rf_accuracies.values()))
plt.title('Random Forest Classifier Accuracy for Different Number of Estimators')
plt.xlabel('Number of Estimators')
plt.ylabel('Accuracy')
plt.xticks(estimators)

plt.show()












