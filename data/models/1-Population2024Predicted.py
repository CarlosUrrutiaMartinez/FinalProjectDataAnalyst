import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023]).reshape(-1, 1)

population = np.array([7.53, 7.63, 7.71, 7.79, 7.87, 7.95, 8.03]).reshape(-1, 1)

m2_supply = np.array([13.8, 14.3, 15.3, 18.2, 19.4, 21.7, 21.5]).reshape(-1, 1)

pop_model = LinearRegression()
pop_model.fit(years, population)

future_year = np.array([2024]).reshape(-1, 1)
predicted_population = pop_model.predict(future_year)

m2_model = LinearRegression()
m2_model.fit(years, m2_supply)

predicted_m2 = m2_model.predict(future_year)

print(f"Predicted World Population for 2024: {predicted_population[0][0]:.2f} billion")
print(f"Predicted USD in Circulation (M2) for 2024: {predicted_m2[0][0]:.2f} trillion USD")

date_range = pd.date_range(start='2017-01-01', end='2024-12-31', freq='D')
df = pd.DataFrame(date_range, columns=['Date'])
df.set_index('Date', inplace=True)

population_daily = np.linspace(7.53, predicted_population[0][0], len(date_range))
m2_daily = np.linspace(13.8, predicted_m2[0][0], len(date_range))

df['World_Population'] = population_daily
df['USD_in_Circulation'] = m2_daily

age_0_17 = 0.26
age_17_64 = 0.65
age_65_plus = 0.09

df['Age_0_17'] = df['World_Population'] * age_0_17
df['Age_17_64'] = df['World_Population'] * age_17_64
df['Age_65_plus'] = df['World_Population'] * age_65_plus

df.to_csv('dataset_poblacion_m2.csv')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(years, population, 'o', label='Historical Data')
plt.plot(future_year, predicted_population, 'o', label='2024 Prediction')
plt.plot(range(2017, 2025), pop_model.predict(np.array(range(2017, 2025)).reshape(-1, 1)), label='Trend Line')
plt.title('World Population')
plt.xlabel('Year')
plt.ylabel('Billions')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(years, m2_supply, 'o', label='Historical Data')
plt.plot(future_year, predicted_m2, 'o', label='2024 Prediction')
plt.plot(range(2017, 2025), m2_model.predict(np.array(range(2017, 2025)).reshape(-1, 1)), label='Trend Line')
plt.title('USD in Circulation (M2)')
plt.xlabel('Year')
plt.ylabel('Trillions of USD')
plt.legend()

plt.tight_layout()
plt.show()
