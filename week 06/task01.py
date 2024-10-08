
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Customer_id=np.random.randint(1000,10000,1000)
Age=np.random.randint(18,70,1000)
Anual_income=np.random.randint(20000,120000,1000)
Gender=np.random.choice(['Male','Female'],1000) 
Purchased=np.random.choice([0,1],1000)

data=pd.DataFrame({'Customer_id':Customer_id,'Age':Age,'Anual_income':Anual_income,'Purchased':Purchased,'Gender':Gender})

print(data.head(10))

# detect missionf values in data set
print(data.isnull().sum())


# fill annual income with mean value

data['Anual_income'].fillna(data['Anual_income'].mean())

# convertion

valaues = data['Gender'].map({'Male': 0, 'Female': 1})


# Scaling

scale_age=(data['Age']-data['Age'].min() ) /( data['Age'].max()-  data['Age'].min())
scale_income=(data['Anual_income']-data['Anual_income'].min()) / (data['Anual_income'].max()-data['Anual_income'].min())

# print("Scaled Age"),print(scale_age)   
# print("Scaled Income"),print(scale_income)

# histogram

plt.hist(data['Age'],bins=10)
# plt.show()


#cors
cors=data[['Age','Anual_income','Purchased']].corr()
print(cors)

# income by age

data['Income_per_Age']=data['Anual_income']/data['Age']
print(data.head(10))

# Drop the CustomerID column as it is irrelevant for prediction
data.drop('Customer_id',inplace=True,axis=1)

print(data.head())

from sklearn.model_selection import train_test_split

# Split the data into features and target variable



# Split the data into training and testing sets (80% training, 20% testing)
X_tran,X_test=train_test_split(data,test_size=0.2,random_state=42)

print(X_tran.head())
print(X_test.head())











