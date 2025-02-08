import pandas as pd

date_df = pd.read_csv('market_dates.csv')

sp500_df = pd.read_csv('sp500_data.csv')
btc_df = pd.read_csv('bitcoin_data.csv')
bond_df = pd.read_csv('us_bonds_data.csv')

def merge_with_dates(market_df, market_name):
    df = date_df.merge(market_df, how='left', on='Date')
    df['Market'] = market_name
    df.fillna({'Price': 0, 'Volume': 0, 'Volatility': 0, 'Price-to-Volume Ratio': 0, 'SMA_50': 0}, inplace=True)
    return df

sp500_df = merge_with_dates(sp500_df, 'SP500')
btc_df = merge_with_dates(btc_df, 'Bitcoin')
bond_df = merge_with_dates(bond_df, 'US Bonds')

final_df = pd.concat([sp500_df, btc_df, bond_df], axis=0)

final_df.to_csv('market_comparison_with_indicators.csv', index=False, encoding='utf-8', sep=',')

print("✅ Archivo final 'market_comparison_with_dates.csv' creado correctamente.")
