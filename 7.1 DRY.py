print("=== Built-in Functions Demonstration ===\n")


my_list = [10, 20, 30, 40, 50]
list_length = len(my_list)
print(f"The list {my_list} has {list_length} elements")


user_name = input("\nWhat's your name? ")
print(f"Hello, {user_name}!")


number = 42
text = "Hello"
decimal = 3.14
print(f"\nThe type of {number} is: {type(number)}")
print(f"The type of '{text}' is: {type(text)}")
print(f"The type of {decimal} is: {type(decimal)}")


negative_num = -25
positive_num = 15
temperature_diff = abs(-5 - 20)  

print(f"\nThe absolute value of {negative_num} is: {abs(negative_num)}")
print(f"The absolute value of {positive_num} is: {abs(positive_num)}")
print(f"Temperature difference: {temperature_diff} degrees")
