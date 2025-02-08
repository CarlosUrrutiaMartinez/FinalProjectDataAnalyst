import pandas as pd
import matplotlib.pyplot as plt

file_name = "merged_full_data_2017_2028.csv"
df = pd.read_csv(file_name)

df['Date'] = pd.to_datetime(df['Date'])

df = df[df['OpenMarket'] == 1]

markets = df['Market'].unique()

for market in markets:
    market_df = df[df['Market'] == market]
    
    plt.figure(figsize=(12, 6))
    plt.plot(market_df['Date'], market_df['Price'], marker='o', linestyle='-', label=f'Precio {market}')

    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.title(f'Evolución del Precio de {market} (2017-2028)')
    plt.legend()
    plt.grid(True)
    plt.show()

