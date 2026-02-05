import random

def fortune():
    """Print a random fortune using list indexing."""
    fortunes = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!"
    ]
    
    print(fortunes[random.randint(0, len(fortunes) - 1)])

# Call the bonus fortune function three times
print("\n Fortune Cookie #1:")
fortune()

print("\n Fortune Cookie #2:")
fortune()

print("\n Fortune Cookie #3:")
fortune()