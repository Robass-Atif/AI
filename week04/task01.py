import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



date=pd.date_range(start='1/1/2018', end='12/31/2018')

temperature=np.random.uniform(10,40,size=365)
humididty=np.random.uniform(30,90,size=365)

wind_speed = np.random.uniform(0, 20, size=365)
weather_condition = np.random.choice(['Sunny', 'Rainy', 'Cloudy'], size=365)

df=pd.DataFrame({'date':date, 'temperature':temperature, 'humidity':humididty, 'wind_speed':wind_speed, 'weather_condition':weather_condition})

print(df.head())


# get tempurature and find mean


temperature_mean = df['temperature'].values

print('Mean temperature:', np.mean(temperature_mean))


avg_temp = len(df[(df['temperature'] > 30) & (df['weather_condition']=='Sunny')])

print('Average temperature greater than 30 and weather condition is sunny:', avg_temp)


# get average humidity by weather condition
avg_humidity_by_weather = df.groupby('weather_condition')['humidity'].mean()


print('Average Humidity by Weather Condition:', avg_humidity_by_weather)


# matplotlib tassk

plt.plot(df['date'], df['temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature variation')
plt.grid(True)

plt.show()

# using bar graph

values=df['weather_condition'].value_counts()
print(values)

plt.bar(values.index, values.values)
plt.show()




