import pandas as pd
import numpy as np

historical_bonds_path = "us_bonds_data_machine_learning.csv"
forecast_bonds_path = "us_bonds_forecast_cycle.csv"

historical_bonds_df = pd.read_csv(historical_bonds_path)
forecast_bonds_df = pd.read_csv(forecast_bonds_path)

historical_bonds_df["Date"] = pd.to_datetime(historical_bonds_df["Date"])
forecast_bonds_df["Date"] = pd.to_datetime(forecast_bonds_df["Date"])

historical_bonds_df = historical_bonds_df[historical_bonds_df["OpenMarket"] == 1]

last_known_price = historical_bonds_df.iloc[-1]["Price"]

historical_bonds_df["CycleYear"] = historical_bonds_df["year"] % 4
forecast_bonds_df["CycleYear"] = forecast_bonds_df["year"] % 4
forecast_bonds_df["CycleMonth"] = forecast_bonds_df["month"] % 12  # Ciclo mensual

bond_targets = {
    1: 3.8,
    2: 3.5,
    3: 4.5,
    0: 5.5
}

monthly_fluctuation = {
    1: (3.8, 4.0),
    2: (3.5, 3.8),
    3: (3.8, 4.5),
    0: (4.5, 5.5)
}

forecast_bonds_df.loc[forecast_bonds_df.index[0], "Price"] = last_known_price

for i in range(1, len(forecast_bonds_df)):
    cycle = forecast_bonds_df.iloc[i]["CycleYear"]
    target_price = bond_targets[cycle]

    min_monthly, max_monthly = monthly_fluctuation[cycle]

    previous_price = forecast_bonds_df.iloc[i - 1]["Price"]
    step = (target_price - last_known_price) / 12

    monthly_variation = np.random.uniform(0.99, 1.01)
    noise_factor = np.random.uniform(-0.05, 0.05)

    new_price = previous_price + step * monthly_variation + noise_factor

    new_price = min(max(new_price, min_monthly), max_monthly)

    forecast_bonds_df.loc[forecast_bonds_df.index[i], "Price"] = new_price

forecast_bonds_df["Price"] = forecast_bonds_df["Price"].rolling(window=10, min_periods=1).mean()

forecast_bonds_path_corrected = "us_bonds_forecast_cycle.csv"
forecast_bonds_df.to_csv(forecast_bonds_path_corrected, index=False)
