import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

sp500_df = pd.read_csv('sp500_forecast_cycle.csv')
btc_df = pd.read_csv('bitcoin_forecast_cycle.csv')
bond_df = pd.read_csv('us_bonds_forecast_cycle.csv')

def adjust_column_order(df):
    column_order = [
        'Date', 'Price', 'Volume', 'Market', 'Volatility', 'Price-to-Volume Ratio', 'SMA_50', 
        'OpenMarket', 'year', 'month', 'day', 'World_Population', 'USD_in_Circulation', 'Age_0_17', 
        'Age_17_64', 'Age_65_plus'
    ]
    df = df[column_order]
    return df

sp500_df = adjust_column_order(sp500_df)
btc_df = adjust_column_order(btc_df)
bond_df = adjust_column_order(bond_df)

sp500_df.to_csv('sp500_forecast_cycle.csv', index=False, encoding='utf-8', sep=',')
btc_df.to_csv('bitcoin_forecast_cycle.csv', index=False, encoding='utf-8', sep=',')
bond_df.to_csv('us_bonds_forecast_cycle.csv', index=False, encoding='utf-8', sep=',')

print("✅ Archivos de mercado con el orden de columnas actualizado correctamente.")
