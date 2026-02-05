class City:
  def __init__(self, name, country, population, landmarks, oldnames, foundingyear, mayor):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.oldnames = oldnames
    self.foundingyear = foundingyear
    self.mayor = mayor

tallinn = City("Tallinn", "Estonia", 462000, ["Alexander Nevsky Cathedral", "Tallinn Old Town"], ["Reval", "Lindanise"], 1219, "Peeter Raudsepp")
rome = City("Rome", "Italy", 2750000, ["Colosseum", "Trevi Fountain", "Pantheon"], ["Roma"], -753, "Roberto Gualtieri")

print(vars(tallinn))
print(vars(rome))

