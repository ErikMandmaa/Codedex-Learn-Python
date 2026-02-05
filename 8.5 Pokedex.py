class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, level, region, weight, height):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.level = level
        self.region = region
        self.weight = weight
        self.height = height

    def speak(self):
        print(f"{self.name}! {self.name}!")

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")

        if len(self.types) == 1:
            print(f"Type: {self.types[0]}")
        else:
            print(f"Type: {', '.join(self.types)}")

        print(f"Description: {self.description}")
        print(f"Level: {self.level}")
        print(f"Region: {self.region}")
        print(f"Weight: {self.weight} lbs")
        print(f"Height: {self.height} ft")

        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")


bulbasaur = Pokemon(
    entry=1,
    name="Bulbasaur",
    types=["Grass", "Poison"],
    description=(
        "A strange seed was planted on its back at birth. The plant sprouts and grows"
        " with this Pokémon."
    ),
    is_caught=True,
    level=5,
    region="Kanto",
    weight=15.2,
    height=2.0,
)

charmander = Pokemon(
    entry=4,
    name="Charmander",
    types=["Fire"],
    description=(
        "Obviously prefers hot places. When it rains, steam is said to spout from the tip"
        " of its tail."
    ),
    is_caught=False,
    level=8,
    region="Kanto",
    weight=18.7,
    height=2.3,
)

pikachu = Pokemon(
    entry=25,
    name="Pikachu",
    types=["Electric"],
    description=(
        "When several of these Pokémon gather, their electricity could build and cause"
        " lightning storms."
    ),
    is_caught=True,
    level=10,
    region="Kanto",
    weight=13.2,
    height=1.4,
)


print("Bulbasaur")
bulbasaur.speak()
print()
bulbasaur.display_details()

print("Charmander")
charmander.speak()
print()
charmander.display_details()

print("Pikachu")
pikachu.speak()
print()
pikachu.display_details()