import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime

sp500_df = pd.read_csv('sp500_data.csv')
btc_df = pd.read_csv('bitcoin_data.csv')
bond_df = pd.read_csv('us_bonds_data.csv')

def create_forecast_df(market_name, market_df, start_year=2025, years_ahead=4):
    future_dates = pd.date_range(start=f'{start_year}-01-01', periods=years_ahead*365, freq='D')
    future_df = pd.DataFrame(future_dates, columns=['Date'])
    
    if market_name == 'SP500' or market_name == 'US Bonds':
        future_df['OpenMarket'] = future_df['Date'].apply(lambda x: 0 if x.weekday() >= 5 else 1)
    elif market_name == 'Bitcoin':
        future_df['OpenMarket'] = 1
    
    population_model = LinearRegression()
    years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023]).reshape(-1, 1)
    population = np.array([7.53, 7.63, 7.71, 7.79, 7.87, 7.95, 8.03]).reshape(-1, 1)
    population_model.fit(years, population)
    predicted_population = population_model.predict(np.array(range(start_year, start_year + years_ahead)).reshape(-1, 1))
    future_df['World_Population'] = np.repeat(predicted_population, 365)

    m2_model = LinearRegression()
    m2_supply = np.array([13.8, 14.3, 15.3, 18.2, 19.4, 21.7, 21.5]).reshape(-1, 1)
    m2_model.fit(years, m2_supply)
    predicted_m2 = m2_model.predict(np.array(range(start_year, start_year + years_ahead)).reshape(-1, 1))
    future_df['USD_in_Circulation'] = np.repeat(predicted_m2, 365)

    age_0_17 = 0.30
    age_17_64 = 0.60
    age_65_plus = 0.10
    future_df['Age_0_17'] = future_df['World_Population'] * age_0_17
    future_df['Age_17_64'] = future_df['World_Population'] * age_17_64
    future_df['Age_65_plus'] = future_df['World_Population'] * age_65_plus

    future_df['year'] = future_df['Date'].dt.year
    future_df['month'] = future_df['Date'].dt.month
    future_df['day'] = future_df['Date'].dt.day
    
    future_df['Price'] = np.nan
    future_df['Volume'] = np.nan
    future_df['Volatility'] = np.nan
    future_df['Price-to-Volume Ratio'] = np.nan
    future_df['SMA_50'] = np.nan
    future_df['Market'] = market_name
    
    return future_df

sp500_future_df = create_forecast_df('SP500', sp500_df)
btc_future_df = create_forecast_df('Bitcoin', btc_df)
bond_future_df = create_forecast_df('US Bonds', bond_df)

sp500_future_df.to_csv('sp500_forecast_cycle.csv', index=False, encoding='utf-8', sep=',')
btc_future_df.to_csv('bitcoin_forecast_cycle.csv', index=False, encoding='utf-8', sep=',')
bond_future_df.to_csv('us_bonds_forecast_cycle.csv', index=False, encoding='utf-8', sep=',')

print("✅ Archivos de predicción para los 3 mercados ('sp500_forecast.csv', 'bitcoin_forecast.csv', 'us_bonds_forecast.csv') creados correctamente.")
