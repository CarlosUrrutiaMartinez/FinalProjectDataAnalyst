CREATE DATABASE finance_project;
CREATE USER 'user2'@'localhost' IDENTIFIED BY 'FinalProject';
GRANT ALL PRIVILEGES ON finance_project.* TO 'user2'@'localhost';
FLUSH PRIVILEGES;
USE finance_project;
SELECT * FROM market_data LIMIT 150;

SELECT 
    Market, 
    Year, 
    ROUND(AVG(Rentability) * 100, 2) AS Avg_Rentability_Percentage
FROM market_data
WHERE Rentability <> 0  -- Excluir rentabilidad 0
AND OpenMarket = 1  -- Solo días en que el mercado estaba abierto
AND Year < 2025  -- Excluir años 2025, 2026, 2027 y 2028
GROUP BY Market, Year
ORDER BY Year;

SELECT 
    Market, 
    ROUND(AVG(Rentability) * 100, 2) AS Total_Avg_Rentability_Percentage
FROM market_data
WHERE Rentability <> 0  -- Excluir rentabilidad 0
AND OpenMarket = 1  -- Solo días en que el mercado estaba abierto
AND Year BETWEEN 2017 AND 2024  -- Solo incluir años 2017 a 2024
GROUP BY Market
ORDER BY Total_Avg_Rentability_Percentage DESC;

SELECT 
    Market, 
    ROUND(STDDEV(Rentability) * 100, 2) AS Rentability_Volatility_Percentage
FROM market_data
WHERE Rentability <> 0  
AND OpenMarket = 1  
AND Year BETWEEN 2017 AND 2024  
AND Market IN ('Bitcoin', 'SP500')  -- Solo incluir Bitcoin y S&P 500
GROUP BY Market
ORDER BY Rentability_Volatility_Percentage DESC;

SELECT 
    Market, 
    Year, 
    ROUND(STDDEV(Rentability) * 100, 2) AS Rentability_Volatility_Percentage
FROM market_data
WHERE Rentability <> 0  
AND OpenMarket = 1  
AND Year BETWEEN 2017 AND 2024  
AND Market IN ('Bitcoin', 'SP500')  -- Excluir US Bonds
GROUP BY Market, Year
ORDER BY Rentability_Volatility_Percentage DESC;

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




