import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


employee_ids = np.random.randint(1000, 10000, size=1500)
ages = np.random.randint(22, 61, size=1500)
years_of_experience = np.random.randint(1, 41, size=1500)
genders = np.random.choice(['Male', 'Female'], size=1500)
performance_ratings = np.random.randint(1, 6, size=1500)  

# Create the DataFrame
data = pd.DataFrame({'Employee_ID': employee_ids, 'Age': ages, 'Years_of_Experience': years_of_experience,'Gender':genders, 'Performance_Rating': performance_ratings})
print(data.head(10))






