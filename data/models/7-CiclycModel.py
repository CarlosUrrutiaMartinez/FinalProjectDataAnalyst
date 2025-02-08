import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression

markets = {
    "Bitcoin": "bitcoin_forecast_cycle.csv",
    "SP500": "sp500_forecast_cycle.csv",
    "US Bonds": "us_bonds_forecast_cycle.csv"
}

best_params = {
    "hidden_layer_sizes": (100, 100),
    "activation": "relu",
    "solver": "adam",
    "max_iter": 1500,
    "random_state": 42
}

historical_growth = {
    "Bitcoin": {
        0: np.linspace(1.05, 1.20, 12).tolist(),
        1: np.linspace(1.02, 1.07, 12).tolist(),
        2: np.linspace(0.93, 0.98, 12).tolist(),
        3: np.linspace(0.92, 0.97, 12).tolist()
    },
    "SP500": np.linspace(1.005, 1.010, 12).tolist(),
    "US Bonds": 1.01
}

def get_halving_cycle(year):
    halving_years = [2012, 2016, 2020, 2024, 2028, 2032]
    last_halving = max([y for y in halving_years if y <= year])
    return (year - last_halving) % 4

for market, file in markets.items():
    print(f"Generando predicciones para {market}...")

    future_df = pd.read_csv(file, delimiter=',', dtype={
        "Price": float,
        "Volume": float,
        "year": int,
        "month": int,
        "day": int,
        "World_Population": float,
        "USD_in_Circulation": float,
        "Age_0_17": float,
        "Age_17_64": float,
        "Age_65_plus": float
    }).copy()

    if market == "Bitcoin":
        future_df["HalvingCycle"] = future_df["year"].apply(get_halving_cycle)
    
    if market != "Bitcoin":
        future_df = future_df[future_df['OpenMarket'] == 1]
    
    historical_file = market.lower().replace(" ", "_") + "_data_machine_learning.csv"
    historical_df = pd.read_csv(historical_file, delimiter=',', dtype={
        "Price": float,
        "Volume": float,
        "year": int,
        "month": int,
        "day": int
    }).copy()

    if market == "Bitcoin":
        historical_df["HalvingCycle"] = historical_df["year"].apply(get_halving_cycle)
    
    historical_df = historical_df[historical_df['OpenMarket'] == 1]
    historical_df = historical_df.dropna(subset=['Price', 'Volume'])
    
    X_future = future_df[['year', 'month', 'day']].copy()
    if market == "Bitcoin":
        X_future["HalvingCycle"] = future_df["HalvingCycle"]
    
    if market == "US Bonds":
        model_bonds = LinearRegression()
        X_train_bonds = historical_df[['year', 'month', 'day']].copy()
        y_train_bonds = historical_df['Price']
        
        model_bonds.fit(X_train_bonds, y_train_bonds)
        
        future_df['Price'] = model_bonds.predict(X_future)
        
        future_df['Price'] = future_df['Price'].rolling(window=30, min_periods=1).mean()
        
    else:
        X_train = historical_df[['year', 'month', 'day']].copy()
        y_train_price = historical_df['Price']
        y_train_volume = historical_df['Volume']
        
        if market == "Bitcoin":
            X_train["HalvingCycle"] = historical_df["HalvingCycle"]
        
        valid_indices_price = ~y_train_price.isna()
        X_train_price = X_train.loc[valid_indices_price].copy()
        y_train_price = y_train_price.loc[valid_indices_price]
        
        valid_indices_volume = ~y_train_volume.isna()
        X_train_volume = X_train.loc[valid_indices_volume].copy()
        y_train_volume = y_train_volume.loc[valid_indices_volume]
        
        price_mean = y_train_price.mean()
        price_std = y_train_price.std()
        y_train_price = (y_train_price - price_mean) / price_std
        
        volume_mean = y_train_volume.mean()
        volume_std = y_train_volume.std()
        y_train_volume = (y_train_volume - volume_mean) / volume_std
        
        model_price = MLPRegressor(**best_params)
        model_volume = MLPRegressor(**best_params)
        
        model_price.fit(X_train_price, y_train_price)
        model_volume.fit(X_train_volume, y_train_volume)
        
        future_df['Price'] = model_price.predict(X_future) * price_std + price_mean
        future_df['Volume'] = model_volume.predict(X_future) * volume_std + volume_mean
        
        last_known_price = historical_df.iloc[-1]['Price']
        future_df.loc[future_df.index[0], 'Price'] = last_known_price
        
        for i in range(1, len(future_df)):
            if market == "Bitcoin":
                cycle = future_df.iloc[i]['HalvingCycle']
                month_index = (future_df.iloc[i]['month'] - 1)
                growth_factor = float(historical_growth["Bitcoin"][cycle][month_index])
                
                monthly_variation = np.random.uniform(0.95, 1.05) if cycle in [1, 2, 3] else np.random.uniform(0.98, 1.02)
                
                growth_factor *= monthly_variation
            
            else:
                growth_factor = float(historical_growth[market][future_df.iloc[i]['month'] - 1])
            
            if future_df.iloc[i]['month'] != future_df.iloc[i-1]['month']:
                future_df.loc[future_df.index[i], 'Price'] = future_df.iloc[i-1]['Price'] * growth_factor
            else:
                future_df.loc[future_df.index[i], 'Price'] = future_df.iloc[i-1]['Price'] * np.random.uniform(0.99, 1.01)

    future_df['Price'] = future_df['Price'].rolling(window=15, min_periods=1).mean()
    
    future_df.to_csv(file, index=False, encoding='utf-8', sep=',')
    print(f"✅ Predicciones guardadas en {file}")

print("🚀 Predicciones completadas para los años 2025-2028.")



