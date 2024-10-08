import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ["John", "Alice", "Bob", "Emily", "Michael", "Sarah", "David", "Jessica", "Daniel", "Sophia", "James", "Olivia", "Andrew", "Mia", "Matthew", "Isabella", "Joshua", "Charlotte", "Ethan", "Liam", "Ava"]
departments = ["HR", "IT", "Sales", "Marketing", "Finance"]

Employee_ID = np.random.randint(1000, 9999, size=1000)
Employee_Name = np.random.choice(names, size=1000)
Department = np.random.choice(departments, size=1000)
Salary = np.random.randint(30000, 100000, size=1000)

Experience = np.random.randint(0, 10, size=1000)

df = pd.DataFrame({'Employee_ID': Employee_ID, 'Employee_Name': Employee_Name, 'Department': Department, 'Salary': Salary, 'Experience': Experience})

print(df.head())

salary_array = df['Salary'].to_numpy()


average_salary = np.mean(salary_array)
max_salary = np.max(salary_array)


min_salary = np.min(salary_array)

print('Average Salary:', average_salary)
print('Max Salary:', max_salary)


print('Min Salary:', min_salary)

filtered_employees = df[(df['Experience'] > 5) & (df['Salary'] > average_salary)]
print(filtered_employees)


mean_salary_by_department = df.groupby('Department')['Salary'].mean()
print(mean_salary_by_department)

plt.bar(mean_salary_by_department.index, mean_salary_by_department.values)
plt.show()

result = df.groupby('Experience')['Salary'].sum()

plt.plot(result.index, result.values)
plt.show()
