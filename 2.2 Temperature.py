def fahrenheit_to_celsius(x):
  celsius = (x - 32) / 1.8
  return celsius

# Current temperature in Brooklyn, NY
temp_f = 81

# Convert to Celsius
temp_c = fahrenheit_to_celsius(temp_f)

print(f"Brooklyn, NY Temperature: {temp_f}°F")
print(f"Converted Temperature: {temp_c:.1f}°C")