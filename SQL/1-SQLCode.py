import pymysql
import pandas as pd
import numpy as np

MYSQL_HOST = "localhost"
MYSQL_USER = "user2"
MYSQL_PASSWORD = "FinalProject"
MYSQL_DB = "finance_project"

conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
cursor = conn.cursor()

file_path = "merged_full_data_2017_2028_with_rentability.xlsx"
df = pd.read_excel(file_path)

df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

df = df.replace({np.nan: None, np.inf: None, -np.inf: None})

expected_columns = [
    "Date", "Price", "Volume", "Market", "Volatility",
    "Price-to-Volume Ratio", "SMA_50", "OpenMarket", "year", "month", "day",
    "World_Population", "USD_in_Circulation", "Age_0_17", "Age_17_64",
    "Age_65_plus", "Rentability"
]

df = df[expected_columns]

print("Column Data Types Before Insertion:")
print(df.dtypes)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS market_data (
        Date DATE,
        Price FLOAT,
        Volume FLOAT NULL,
        Market VARCHAR(50),
        Volatility FLOAT NULL,
        Price_to_Volume FLOAT NULL,
        SMA_50 FLOAT NULL,
        OpenMarket TINYINT,
        Year INT,
        Month INT,
        Day INT,
        World_Population FLOAT NULL,
        USD_in_Circulation FLOAT NULL,
        Age_0_17 FLOAT NULL,
        Age_17_64 FLOAT NULL,
        Age_65_plus FLOAT NULL,
        Rentability FLOAT NULL,
        PRIMARY KEY (Date, Market)
    )
''')

print("Sample row before insertion:", df.iloc[0].to_dict())

for row in df.itertuples(index=False, name=None):
    try:
        row = tuple(None if isinstance(value, float) and (np.isnan(value) or np.isinf(value)) else value for value in row)

        cursor.execute('''
            INSERT INTO market_data (Date, Price, Volume, Market, Volatility, Price_to_Volume, 
            SMA_50, OpenMarket, Year, Month, Day, World_Population, USD_in_Circulation, 
            Age_0_17, Age_17_64, Age_65_plus, Rentability)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE Price=VALUES(Price), Volume=VALUES(Volume), Rentability=VALUES(Rentability);
        ''', row)
    except Exception as e:
        print("Error inserting row:", row)
        print("MySQL Error:", e)

conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into MySQL!")
