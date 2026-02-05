def get_item(x):
    if x == 1:
        return "You ordered a Cheeseburger."
    elif x == 2:
        return "You ordered Fries."
    elif x == 3:
        return "You ordered a Soda."
    elif x == 4:
        return "You ordered Ice Cream."
    elif x == 5:
        return "You ordered a Cookie."
    else:
        return "Invalid item number. Please try again."

def welcome():
    print("Welcome to the Drive-Thru!")
    print("Menu:")
    print("1. Cheeseburger")
    print("2. Fries")
    print("3. Soda")
    print("4. Ice Cream")
    print("5. Cookie")
    print("Please select an item by entering its number.")

welcome()

option = int(input("What would you like to order? "))
print(get_item(option))

