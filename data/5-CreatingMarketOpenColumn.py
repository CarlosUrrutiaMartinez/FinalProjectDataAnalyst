import pandas as pd

df = pd.read_csv('market_comparison_with_indicators.csv')

df['OpenMarket'] = df['Price'].apply(lambda x: 1 if x != 0 else 0)

df.to_csv('market_comparison_with_indicators.csv', index=False, encoding='utf-8', sep=',')

print("✅ Columna 'OpenMarket' añadida y archivo guardado como 'market_comparison_with_indicators.csv'.")
