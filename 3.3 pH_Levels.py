ph_level = int(input("Enter your ph level: "))
if ph_level > 7:
  print("Basic")
elif ph_level < 7:
  print("Acidic")
else:
  print("Neutral")
