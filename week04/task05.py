# Case Study 5: Stock Market Analysis
# You are working with stock market data containing columns like Date, Open
# Price, Close Price, Volume Traded, and Company.
# 1. Data Generation Task: Generate a dataset with 1000 rows. The Date
# column should contain random dates for the past two years, and the Company column should contain random selections from 5 companies. Assign
# random Open Price and Close Price values between $50 and $500, and
# Volume Traded values between 1000 and 1,000,000.
# 2. NumPy Task: Convert the Close Price column into a NumPy array.
# Calculate the daily percentage change in stock prices.
# 3. Pandas Task: Filter the data to find all the days when the stock price
# increased by more than 2% compared to the previous day.
# 4. Pandas Task: Group the data by Company and calculate the total Volume Traded for each company.
# 5. Matplotlib Task: Plot a line graph showing the trend of the Close Price
# over time for a particular company.
# 6. Matplotlib Task: Create a bar chart to compare the average percentage
# change in Close Price for different companies.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Dates=np.random.choice(pd.date_range(start='1/1/2019', end='12/31/2020', periods=1000),size=1000)
Company=np.random.choice(['Apple','Google','Microsoft','Amazon','Facebook'],size=1000)
Open_Price=np.random.randint(50,500,size=1000)
Close_Price=np.random.randint(50,500,size=1000)
Volume_Traded=np.random.randint(1000,1000000,size=1000)

df=pd.DataFrame({'Dates':Dates, 'Company':Company, 'Open_Price':Open_Price, 'Close_Price':Close_Price, 'Volume_Traded':Volume_Traded})


# second

close_price_array = df['Close_Price'].to_numpy()

percentage_change = np.round(np.diff(close_price_array) / close_price_array[:-1] * 100, 2)

# print 5 values
print(percentage_change[:5])


# third



# fourth

company_Data = df.groupby('Company')['Volume_Traded'].sum()
print('Total Volume Traded by Company:', company_Data)

# fifth

company=df[df['Company']=='Google']


plt.plot(company['Dates'],company['Close_Price'])

plt.xlabel('Dates')
plt.show()


df['Percentage Change'] = df.groupby('Company')['Close_Price'].pct_change() * 100

avg= df.groupby('Company')['Percentage Change'].mean()

plt.bar(avg.index,avg.values)
plt.show()







