class bobsburgers:
    def __init__(self):
        self.name = "Bob\'s Burgers"
        self.category = "American Diner"
        self.rating = 4.7
        self.delivery = False

class burgerjoint:
    def __init__(self):
        self.name = "Burger Joint"
        self.category = "Fast Food"
        self.rating = 4.3
        self.delivery = True

class pizzapalace:
    def __init__(self):
        self.name = "Pizza Palace"
        self.category = "Italian"
        self.rating = 4.5
        self.delivery = True

restaurants = [bobsburgers(), burgerjoint(), pizzapalace()]

for restaurant in restaurants:
    print(vars(restaurant))