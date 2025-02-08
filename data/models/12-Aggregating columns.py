import pandas as pd

file_path = "merged_full_data_2017_2028.xlsx"
df = pd.read_excel(file_path)

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values(by=["Market", "Date"])

df["Rentability"] = None

for market in df["Market"].unique():
    market_data = df[df["Market"] == market].copy()

    market_data["Prev_Price"] = market_data["Price"].shift(1)

    market_data["Prev_Price"] = market_data["Prev_Price"].fillna(method="ffill")

    market_data["Rentability"] = (market_data["Price"] - market_data["Prev_Price"]) / market_data["Prev_Price"] * 100
    market_data.loc[market_data["Prev_Price"] == 0, "Rentability"] = 0

    df.loc[df["Market"] == market, "Rentability"] = market_data["Rentability"]

corrected_file_path = "merged_full_data_2017_2028_with_rentability.xlsx"
df.to_excel(corrected_file_path, index=False)
