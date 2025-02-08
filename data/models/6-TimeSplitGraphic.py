import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast(file_name, market_name):
    df = pd.read_csv(file_name)

    df['Date'] = pd.to_datetime(df['Date'])

    numeric_columns = df.select_dtypes(include=['number']).columns

    df_monthly = df.set_index('Date').resample('ME')[numeric_columns].mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df_monthly.index, df_monthly['Price'], marker='o', linestyle='-', label=f'Precio {market_name}')

    plt.xlabel('Fecha')
    plt.ylabel(f'Precio de {market_name}')
    plt.title(f'Predicción del Precio de {market_name} (2025-2028)')
    plt.legend()
    plt.grid(True)

    plt.show()

forecast_files = {
    "Bitcoin": "bitcoin_forecast.csv",
    "SP500": "sp500_forecast.csv",
    "US Bonds": "us_bonds_forecast.csv"
}

for market, file in forecast_files.items():
    plot_forecast(file, market)
