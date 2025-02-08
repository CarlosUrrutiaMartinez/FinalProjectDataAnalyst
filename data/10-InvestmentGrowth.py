import matplotlib.pyplot as plt

initial_investment = 30000

return_rate_high = 0.10
return_rate_low = 0.03

years = list(range(2017, 2025))

def compound_interest(principal, rate, years):
    values = [principal]
    for _ in range(len(years) - 1):
        new_value = values[-1] * (1 + rate)
        values.append(new_value)
    return values

investment_high = compound_interest(initial_investment, return_rate_high, years)
investment_low = compound_interest(initial_investment, return_rate_low, years)

plt.figure(figsize=(10, 6))
plt.plot(years, investment_high, label='Investment Growth (10% Return)', marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Investment Value (monetary units)')
plt.title('Investment Growth with a 10% Annual Return (2017-2024)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(years, investment_low, label='Investment Growth (3% Return)', marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Investment Value (monetary units)')
plt.title('Investment Growth with a 3% Annual Return (2017-2024)')
plt.legend()
plt.grid(True)
plt.show()
