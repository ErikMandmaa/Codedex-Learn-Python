import random 

def bday_messages():
    messages = [
        "Hope you have a very Happy Birthday! 🎈",
        "It's your special day – get out there and celebrate! 🎉",
        "You were born and the world got better – everybody wins! 🥳",
        "Have lots of fun on your special day! 🎂",
        "Another year of you going around the sun! 🌞"
    ]
    return random.choice(messages)

random_message = bday_messages()
print(random_message)