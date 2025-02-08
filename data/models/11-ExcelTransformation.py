import pandas as pd

csv_file_path = "merged_full_data_2017_2028.csv"
df = pd.read_csv(csv_file_path, dtype={
    "Price": float,
    "Volume": float,
    "Volatility": float,
    "Price-to-Volume Ratio": float,
    "SMA_50": float,
    "World_Population": float,
    "USD_in_Circulation": float,
    "Age_0_17": float,
    "Age_17_64": float,
    "Age_65_plus": float,
    "HalvingCycle": "Int64",
    "CycleYear": "Int64",
    "CycleMonth": "Int64"
})

df["Date"] = pd.to_datetime(df["Date"])

excel_file_path = "merged_full_data_2017_2028.xlsx"
df.to_excel(excel_file_path, index=False, sheet_name="Data")

print(f"✅ Archivo Excel guardado en: {excel_file_path}")
