import pandas as pd

date_range = pd.date_range(start="2017-01-01", end="2024-12-31", freq="D")

date_df = pd.DataFrame(date_range, columns=["Date"])

date_df.to_csv('market_dates.csv', index=False, encoding='utf-8', sep=',')

print("✅ CSV de fechas generado correctamente.")

