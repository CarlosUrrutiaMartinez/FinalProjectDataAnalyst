import yfinance as yf 
import pandas as pd
from fredapi import Fred

fred_api_key = '79cb4f6fa8eda3b1fe4d1075e65b48c9'  # Sustituye con tu clave real
fred = Fred(api_key=fred_api_key)

def get_sp500_data():
    sp500 = yf.download('^GSPC', start='2017-01-01', end='2024-12-31')
    sp500 = sp500[['Close', 'Volume']].copy()
    sp500.rename(columns={'Close': 'Price', 'Volume': 'Volume'}, inplace=True)
    sp500['Market'] = 'SP500'
    sp500.index = sp500.index.tz_localize(None)  # Eliminar zona horaria
    return sp500

def get_bitcoin_data():
    bitcoin = yf.Ticker("BTC-USD")
    btc_data = bitcoin.history(start="2017-01-01", end="2024-12-31")
    btc_data = btc_data[['Close', 'Volume']].copy()
    btc_data.rename(columns={'Close': 'Price', 'Volume': 'Volume'}, inplace=True)
    btc_data['Market'] = 'Bitcoin'
    btc_data.index = btc_data.index.tz_localize(None)
    return btc_data

def get_bond_data():
    bond_data = fred.get_series('DGS10') 
    bond_df = pd.DataFrame(bond_data, columns=['Price'])
    
    bond_df = bond_df[(bond_df.index >= '2017-01-01') & (bond_df.index <= '2024-12-31')]
    
    bond_df['Volume'] = 1  
    bond_df['Market'] = 'US Bonds'
    bond_df.index.name = 'Date'
    bond_df.index = bond_df.index.tz_localize(None)


    bond_df['Price'] = bond_df['Price'].interpolate(method='linear')
    return bond_df

sp500_df = get_sp500_data()
btc_df = get_bitcoin_data()
bond_df = get_bond_data()

common_columns = ['Price', 'Volume', 'Market']
sp500_df = sp500_df[common_columns]
btc_df = btc_df[common_columns]
bond_df = bond_df[common_columns]

sp500_df.columns = common_columns
btc_df.columns = common_columns
bond_df.columns = common_columns


sp500_df['Volatility'] = sp500_df['Price'].pct_change().rolling(window=30).std()
btc_df['Volatility'] = btc_df['Price'].pct_change().rolling(window=30).std()
bond_df['Volatility'] = bond_df['Price'].pct_change().rolling(window=30).std()

sp500_df.dropna(subset=['Volatility'], inplace=True)
btc_df.dropna(subset=['Volatility'], inplace=True)
bond_df.dropna(subset=['Volatility'], inplace=True)

sp500_df['Price-to-Volume Ratio'] = sp500_df['Price'] / sp500_df['Volume'].replace(0, 1)
btc_df['Price-to-Volume Ratio'] = btc_df['Price'] / btc_df['Volume'].fillna(1)
bond_df['Price-to-Volume Ratio'] = bond_df['Price'] / bond_df['Volume'].fillna(1)

sp500_df['SMA_50'] = sp500_df['Price'].rolling(window=50).mean().fillna(method='bfill')
btc_df['SMA_50'] = btc_df['Price'].rolling(window=50).mean().fillna(method='bfill')
bond_df['SMA_50'] = bond_df['Price'].rolling(window=50).mean().fillna(method='bfill')

combined_df = pd.concat([sp500_df, btc_df, bond_df], axis=0)

combined_df.columns = ['Price', 'Volume', 'Market', 'Volatility', 'Price-to-Volume Ratio', 'SMA_50']

combined_df.to_csv('market_comparison_with_indicators.csv', index=True, encoding='utf-8', sep=',')

print("✅ Datos guardados correctamente en 'market_comparison_with_indicators.csv'.")






