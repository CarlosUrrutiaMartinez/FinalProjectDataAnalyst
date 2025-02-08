import pandas as pd

date_df = pd.read_csv('market_dates.csv')

sp500_df = pd.read_csv('sp500_data.csv')
btc_df = pd.read_csv('bitcoin_data.csv')
bond_df = pd.read_csv('us_bonds_data.csv')

def merge_with_dates(market_df, market_name):
    df = date_df.merge(market_df, how='left', on='Date')
    df['Market'] = market_name
    df.fillna({'Price': 0, 'Volume': 0, 'Volatility': 0, 'Price-to-Volume Ratio': 0, 'SMA_50': 0}, inplace=True)
    df['OpenMarket'] = df['Price'].apply(lambda x: 1 if x != 0 else 0)

    df['Date'] = pd.to_datetime(df['Date'])
    
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    
    return df

sp500_df = merge_with_dates(sp500_df, 'SP500')
btc_df = merge_with_dates(btc_df, 'Bitcoin')
bond_df = merge_with_dates(bond_df, 'US Bonds')

sp500_df.to_csv('sp500_data.csv', index=False, encoding='utf-8', sep=',')
btc_df.to_csv('bitcoin_data.csv', index=False, encoding='utf-8', sep=',')
bond_df.to_csv('us_bonds_data.csv', index=False, encoding='utf-8', sep=',')

print("✅ Archivos 'sp500_data.csv', 'bitcoin_data.csv' y 'us_bonds_data.csv' actualizados correctamente con las columnas 'OpenMarket', 'year', 'month' y 'day'.")




