import pandas as pd
import pymysql
from tabulate import tabulate

db_config = {
    "host": "localhost",
    "user": "user2",
    "password": "FinalProject",
    "database": "finance_project"
}

connection = pymysql.connect(**db_config)

queries = {
    "all_data": "SELECT * FROM market_data LIMIT 150;",
    
    "avg_rentability_per_year": """
        SELECT 
            Market, 
            Year, 
            ROUND(AVG(Rentability) * 100, 2) AS Avg_Rentability_Percentage
        FROM market_data
        WHERE Rentability <> 0  
        AND OpenMarket = 1  
        AND Year < 2025  
        GROUP BY Market, Year
        ORDER BY Year;
    """,

    "total_avg_rentability": """
        SELECT 
            Market, 
            ROUND(AVG(Rentability) * 100, 2) AS Total_Avg_Rentability_Percentage
        FROM market_data
        WHERE Rentability <> 0  
        AND OpenMarket = 1  
        AND Year BETWEEN 2017 AND 2024  
        GROUP BY Market
        ORDER BY Total_Avg_Rentability_Percentage DESC;
    """,

    "bitcoin_sp500_volatility": """
        SELECT 
            Market, 
            ROUND(STDDEV(Rentability) * 100, 2) AS Rentability_Volatility_Percentage
        FROM market_data
        WHERE Rentability <> 0  
        AND OpenMarket = 1  
        AND Year BETWEEN 2017 AND 2024  
        AND Market IN ('Bitcoin', 'SP500')  
        GROUP BY Market
        ORDER BY Rentability_Volatility_Percentage DESC;
    """,

    "yearly_volatility_bitcoin_sp500": """
        SELECT 
            Market, 
            Year, 
            ROUND(STDDEV(Rentability) * 100, 2) AS Rentability_Volatility_Percentage
        FROM market_data
        WHERE Rentability <> 0  
        AND OpenMarket = 1  
        AND Year BETWEEN 2017 AND 2024  
        AND Market IN ('Bitcoin', 'SP500')  
        GROUP BY Market, Year
        ORDER BY Rentability_Volatility_Percentage DESC;
    """,

    "monthly_avg_rentability": """
        SELECT 
            Market, 
            ELT(Month, 'January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December') AS Month_Name,
            ROUND(AVG(Rentability) * 100, 2) AS Avg_Rentability_Percentage
        FROM market_data
        WHERE Rentability <> 0  
        AND OpenMarket = 1  
        AND Year BETWEEN 2017 AND 2024  
        GROUP BY Market, Month
        ORDER BY Market, Avg_Rentability_Percentage DESC;
    """
}

dataframes = {}
try:
    with connection.cursor() as cursor:
        for key, query in queries.items():
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            dataframes[key] = pd.DataFrame(cursor.fetchall(), columns=columns)

finally:
    connection.close()

for name, df in dataframes.items():
    print(f"\n{name}:\n", df.head())


import matplotlib.pyplot as plt

df_avg_rentability = dataframes["avg_rentability_per_year"]

markets = df_avg_rentability["Market"].unique()

for market in markets:
    df_market = df_avg_rentability[df_avg_rentability["Market"] == market]
    
    plt.figure(figsize=(10, 5))
    plt.plot(df_market["Year"], df_market["Avg_Rentability_Percentage"], marker="o", linestyle="-")
    plt.title(f"Average Rentability Percentage per Year - {market}")
    plt.xlabel("Year")
    plt.ylabel("Avg Rentability (%)")
    plt.grid(True)
    plt.xticks(df_market["Year"])
    plt.show()

df_yearly_volatility = dataframes["yearly_volatility_bitcoin_sp500"]

for market in df_yearly_volatility["Market"].unique():
    df_market = df_yearly_volatility[df_yearly_volatility["Market"] == market]

    plt.figure(figsize=(10, 5))
    plt.plot(df_market["Year"], df_market["Rentability_Volatility_Percentage"], marker="o", linestyle="-")
    plt.title(f"Yearly Volatility Percentage - {market}")
    plt.xlabel("Year")
    plt.ylabel("Volatility Percentage (%)")
    plt.grid(True)
    plt.xticks(df_market["Year"].unique())
    plt.show()

df_monthly_avg_rentability = dataframes["monthly_avg_rentability"]

for market in df_monthly_avg_rentability["Market"].unique():
    df_market = df_monthly_avg_rentability[df_monthly_avg_rentability["Market"] == market]

    plt.figure(figsize=(12, 6))
    plt.plot(df_market["Month_Name"], df_market["Avg_Rentability_Percentage"], marker="o", linestyle="-")
    plt.title(f"Monthly Average Rentability Percentage (2017-2024) - {market}")
    plt.xlabel("Month")
    plt.ylabel("Avg Rentability (%)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()