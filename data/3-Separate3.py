import pandas as pd

combined_df = pd.read_csv('market_comparison_with_indicators.csv')

sp500_df = combined_df[combined_df['Market'] == 'SP500']
sp500_df.to_csv('sp500_data.csv', index=False, encoding='utf-8', sep=',')

btc_df = combined_df[combined_df['Market'] == 'Bitcoin']
btc_df.to_csv('bitcoin_data.csv', index=False, encoding='utf-8', sep=',')

bond_df = combined_df[combined_df['Market'] == 'US Bonds']
bond_df.to_csv('us_bonds_data.csv', index=False, encoding='utf-8', sep=',')

print("✅ Archivos CSV separados generados correctamente.")
