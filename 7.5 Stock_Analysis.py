stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn

print(f"The max price between day 1 and 15 is: {max_price(1, 15)}")
print(f"The min price between day 5 and 10 is: {min_price(5, 10)}")
print(f"The price on day 3 is: {price_at(3)}")