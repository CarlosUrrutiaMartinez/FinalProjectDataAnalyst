import pandas as pd

file_path = "merged_full_data_2017_2028_with_rentability.xlsx"
df = pd.read_excel(file_path)

negative_rentability = df[df["Rentability"] == -100]
print("Cantidad de días con Rentabilidad -100 por mercado:")
print(negative_rentability["Market"].value_counts())

print(negative_rentability.head(20))

import pandas as pd

file_path = "merged_full_data_2017_2028_with_rentability.xlsx"
df = pd.read_excel(file_path)
df["Rentability"] = df["Rentability"].replace(-100, 0)

df.to_excel("merged_full_data_fixed.xlsx", index=False)

print("Corrección realizada: -100 reemplazado por 0 en Rentability.")
