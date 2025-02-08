import pandas as pd

population_df = pd.read_csv('dataset_poblacion_m2.csv')

sp500_df = pd.read_csv('sp500_data.csv')
btc_df = pd.read_csv('bitcoin_data.csv')
bond_df = pd.read_csv('us_bonds_data.csv')


def merge_with_population(market_df):
    df = market_df.merge(population_df, how='left', left_on='Date', right_on='Date')  # Usamos left join para mantener todas las fechas
    df.fillna({'Price': 0, 'Volume': 0, 'Volatility': 0, 'Price-to-Volume Ratio': 0, 'SMA_50': 0}, inplace=True)  # Rellenar con 0 los valores nulos
    return df

sp500_df = merge_with_population(sp500_df)
btc_df = merge_with_population(btc_df)
bond_df = merge_with_population(bond_df)

sp500_df.to_csv('sp500_data_machine_learning.csv', index=False, encoding='utf-8', sep=',')
btc_df.to_csv('bitcoin_data_machine_learning.csv', index=False, encoding='utf-8', sep=',')
bond_df.to_csv('us_bonds_data_machine_learning.csv', index=False, encoding='utf-8', sep=',')

print("✅ Archivos 'sp500_data.csv', 'bitcoin_data.csv' y 'us_bonds_data.csv' fusionados correctamente y sobreescritos.")

