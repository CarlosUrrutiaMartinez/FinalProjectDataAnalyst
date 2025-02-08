import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression

markets = {
    "Bitcoin": "bitcoin_forecast.csv",
    "SP500": "sp500_forecast.csv",
    "US Bonds": "us_bonds_forecast.csv"
}

best_params = {
    "hidden_layer_sizes": (100, 100),
    "activation": "relu",
    "solver": "adam",
    "max_iter": 1500,
    "random_state": 42
}

historical_growth = {
    "Bitcoin": 1.05,
    "SP500": 1.02,
    "US Bonds": 1.01
}

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
    })
    
    if market != "Bitcoin":
        future_df = future_df[future_df['OpenMarket'] == 1]
    
    historical_file = market.lower().replace(" ", "_") + "_data_machine_learning.csv"
    historical_df = pd.read_csv(historical_file, delimiter=',', dtype={
        "Price": float,
        "Volume": float,
        "year": int,
        "month": int,
        "day": int
    })

    historical_df = historical_df[historical_df['OpenMarket'] == 1]
    historical_df = historical_df.dropna(subset=['Price', 'Volume'])
    
    X_future = future_df[['year', 'month', 'day']]
    
    if market == "US Bonds":
        model_bonds = LinearRegression()
        X_train_bonds = historical_df[['year', 'month', 'day']]
        y_train_bonds = historical_df['Price']
        
        model_bonds.fit(X_train_bonds, y_train_bonds)
        
        future_df['Price'] = model_bonds.predict(X_future)
        
        future_df['Price'] = future_df['Price'].rolling(window=30, min_periods=1).mean()
        
    else:
        X_train = historical_df[['year', 'month', 'day']]
        y_train_price = historical_df['Price']
        y_train_volume = historical_df['Volume']

        valid_indices_price = ~y_train_price.isna()
        X_train_price = X_train[valid_indices_price]
        y_train_price = y_train_price[valid_indices_price]
        
        valid_indices_volume = ~y_train_volume.isna()
        X_train_volume = X_train[valid_indices_volume]
        y_train_volume = y_train_volume[valid_indices_volume]
        
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
            if future_df.iloc[i]['month'] != future_df.iloc[i-1]['month']:
                future_df.loc[future_df.index[i], 'Price'] = future_df.iloc[i-1]['Price'] * historical_growth[market]
            else:
                future_df.loc[future_df.index[i], 'Price'] = future_df.iloc[i-1]['Price'] * np.random.uniform(0.98, 1.02)  # Variación diaria ligera
    
    future_df['Volatility'] = future_df['Price'].pct_change().rolling(window=30).std()
    future_df['Price-to-Volume Ratio'] = future_df['Price'] / future_df['Volume'].replace(0, 1)
    future_df['SMA_50'] = future_df['Price'].rolling(window=50).mean().bfill()
    
    future_df.to_csv(file, index=False, encoding='utf-8', sep=',')
    print(f"✅ Predicciones guardadas en {file}")

print("🚀 Predicciones completadas para los años 2025-2028.")




