def pesos_to_dollar(pesos):
    return pesos / 4019.24

def soles_to_dollar(soles):
    return soles / 3.55

def reais_to_dollar(reais):
    return reais / 5.50

# Get user input for each currency
pesos = float(input("What do you have left in pesos? "))
soles = float(input("What do you have left in soles? "))
reais = float(input("What do you have left in reais? "))

# Convert each to USD
usd_from_pesos = pesos_to_dollar(pesos)
usd_from_soles = soles_to_dollar(soles)
usd_from_reais = reais_to_dollar(reais)

# Calculate total in USD
total_usd = usd_from_pesos + usd_from_soles + usd_from_reais

# Display the total
print(total_usd)