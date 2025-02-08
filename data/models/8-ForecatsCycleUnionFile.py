import pandas as pd

files = [
    "bitcoin_forecast_cycle.csv",
    "sp500_forecast_cycle.csv",
    "us_bonds_forecast_cycle.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv("merged_forecast_data.csv", index=False, encoding='utf-8', sep=',')

print("✅ Archivo combinado guardado como merged_forecast_data.csv")

import pandas as pd

historical_files = [
    "bitcoin_data_machine_learning.csv",
    "sp500_data_machine_learning.csv",
    "us_bonds_data_machine_learning.csv"
]

forecast_files = [
    "bitcoin_forecast_cycle.csv",
    "sp500_forecast_cycle.csv",
    "us_bonds_forecast_cycle.csv"
]

dfs = []

for file in historical_files:
    df = pd.read_csv(file)
    dfs.append(df)

for file in forecast_files:
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv("merged_historical_forecast_data.csv", index=False, encoding='utf-8', sep=',')

print("✅ Archivo combinado guardado como merged_historical_forecast_data.csv")

import pandas as pd

historical_files = [
    "bitcoin_data_machine_learning.csv",
    "sp500_data_machine_learning.csv",
    "us_bonds_data_machine_learning.csv"
]

forecast_files = [
    "bitcoin_forecast_cycle.csv",
    "sp500_forecast_cycle.csv",
    "us_bonds_forecast_cycle.csv"
]

dfs = []

for file in historical_files:
    df = pd.read_csv(file)
    dfs.append(df)

for file in forecast_files:
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df = merged_df.sort_values(by='Date')

merged_df.to_csv("merged_full_data_2017_2028.csv", index=False, encoding='utf-8', sep=',')

print("✅ Archivo combinado guardado como merged_full_data_2017_2028.csv")

import pandas as pd

historical_files = [
    "bitcoin_data_machine_learning.csv",
    "sp500_data_machine_learning.csv",
    "us_bonds_data_machine_learning.csv"
]

forecast_files = [
    "bitcoin_forecast_cycle.csv",
    "sp500_forecast_cycle.csv",
    "us_bonds_forecast_cycle.csv"
]

dfs = []

for file in historical_files:
    df = pd.read_csv(file)
    dfs.append(df)

for file in forecast_files:
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df = merged_df.sort_values(by='Date')

merged_df.to_csv("merged_full_data_2017_2028.csv", index=False, encoding='utf-8', sep=',')

print("✅ Archivo combinado guardado como merged_full_data_2017_2028.csv")

