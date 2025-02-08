import matplotlib.pyplot as plt

inflacion_espana = [0.011, 0.012, 0.008, -0.005, 0.065, 0.057, 0.031, 0.028]

inflacion_eeuu = [0.021, 0.024, 0.018, 0.012, 0.047, 0.080, 0.041, 0.029]

valor_inicial = 300000

def calcular_valor(valor_inicial, tasas_inflacion):
    valores = [valor_inicial]
    for tasa in tasas_inflacion:
        nuevo_valor = valores[-1] * (1 + tasa)
        valores.append(nuevo_valor)
    return valores

valores_espana = calcular_valor(valor_inicial, inflacion_espana)
valores_eeuu = calcular_valor(valor_inicial, inflacion_eeuu)

anios = list(range(2017, 2025))

plt.figure(figsize=(10, 6))
plt.plot(anios, valores_espana[:-1], label='Spain', marker='o')
plt.plot(anios, valores_eeuu[:-1], label='USA', marker='o')
plt.xlabel('Year')
plt.ylabel('House Value (monetary units)')
plt.title('Value of 300,000 Monetary Units Adjusted for Inflation (2017-2024)')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

years = list(range(2017, 2025))

inflation_spain = [0.011, 0.012, 0.008, -0.005, 0.065, 0.057, 0.031, 0.028]

inflation_usa = [0.021, 0.024, 0.018, 0.012, 0.047, 0.080, 0.041, 0.029]

plt.figure(figsize=(10, 6))
plt.plot(years, inflation_spain, label='Spain Inflation Rate', marker='o')
plt.plot(years, inflation_usa, label='United States Inflation Rate', marker='o')
plt.xlabel('Year')
plt.ylabel('Inflation Rate')
plt.title('Annual Inflation Rate in Spain and the United States (2017-2024)')
plt.legend()
plt.grid(True)
plt.show()
