import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dates = np.random.choice(pd.date_range(start='1/1/2019', end='12/31/2020', periods=1000), size=1000)
Company = np.random.choice(['Apple', 'Google', 'Microsoft', 'Amazon', 'Facebook'], size=1000)
Open_Price = np.random.randint(50, 500, size=1000)

Close_Price = np.random.randint(50, 500, size=1000)



Volume_Traded = np.random.randint(1000, 1000000, size=1000)

df = pd.DataFrame({'Dates': Dates, 'Company': Company, 'Open_Price': Open_Price, 'Close_Price': Close_Price, 'Volume_Traded': Volume_Traded})

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
company = df[df['Company'] == 'Google']
plt.plot(company['Dates'], company['Close_Price'])
plt.xlabel('Dates')
plt.ylabel('Close Price')
plt.title('Close Price Trend for Google')
plt.show()

df['Percentage Change'] = df.groupby('Company')['Close_Price'].pct_change() * 100
avg = df.groupby('Company')['Percentage Change'].mean()
plt.bar(avg.index, avg.values)
plt.xlabel('Company')
plt.ylabel('Average Percentage Change')
plt.title('Average Percentage Change in Close Price by Company')
plt.show()
