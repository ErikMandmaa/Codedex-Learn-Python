from math import pi
from random import choice as ch

planets = [
  "Mercury",
  "Venus",
  "Earth",
  "Mars",
  "Saturn"
]

def r(random_planet):
    if random_planet == "Mercury":
        return 2440
    elif random_planet == "Venus":
        return 6052
    elif random_planet == "Earth":
        return 6371
    elif random_planet == "Mars":
        return 3390
    elif random_planet == "Saturn":
        return 58232
    else:
        print("Oops! An error has occurred.")

def area(random_planet):
    radius = r(random_planet)
    area = 4 * pi * (radius ** 2)
    return area

random_planet = ch(planets)
print(f"The surface area of {random_planet} is {round(area(random_planet), 0)} square kilometers. ")
