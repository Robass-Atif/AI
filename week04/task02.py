import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

product = np.random.choice(['egg', 'apple', 'bread', 'milk', 'butter', 'mango', 'rice', 'laptop', 'mouse', 'windows'], size=500)
price = np.random.randint(10, 1000, size=500)

quantity = np.random.randint(1, 20, size=500)


dates = pd.date_range(start='1/1/2018', end='12/31/2018', periods=500)



df = pd.DataFrame({'product': product, 'price': price, 'quantity': quantity, 'dates': dates})

# thirds
values = df[['price', 'quantity']].to_numpy()

totalPrice = values[:, 0] * values[:, 1]

df['totalPrice'] = totalPrice

orders = df[df['totalPrice'] > 100]

print(orders)

# fourth
result = df.groupby('product')['totalPrice'].sum()

print(result)

plt.scatter(df['price'], df['quantity'])
plt.show()

# fifth
plt.hist(df['totalPrice'], bins=10)


plt.xlabel('Frequency')


plt.ylabel('Total Price')

plt.show()
