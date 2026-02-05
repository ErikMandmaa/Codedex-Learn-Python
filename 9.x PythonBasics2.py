# Lists
# snow = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8] 

# Index
# day_1 = snow[0] # 0.3
# day_7 = snow[6] # 0.8

# Negative Index
# day_7 = snow[-1] # 0.8
# snow_weekday = snow[ : ] 

# Slicing
# snow_weekday = snow[0:5] # [0.3, 0.0, 0.0, 1.2, 3.9] 
# snow_weekend = snow[5:7] # [2.2, 0.8]

# ----------------------------------------------------------

# Scope
# t = 29 # global scope

# def function():
   # t= 42 # local scope
   # print(t)

# print(t) # output: 29
# function() # output: 42
 
# ----------------------------------------------------------

# List Functions & Methods
# film_runtimes = [121, 142, 131, 124]

# built-in functions
# len(film_runtimes) # output: 4
# max(film_runtimes) # output: 142
# min(film_runtimes) # output: 121

# built-in methods
# film_runtimes.append(152) # film_runtimes is now [121, 142, 131, 124, 152]
# film_runtimes.insert (3, 138) # film runtimes is now [121, 142, 131, 138, 124, 152]
# film_runtimes.remove(142) # film_runtimes is now [121, 131, 138, 124, 152]
# film_runtimes.pop(0) # output: 121, film_runtimes is now [131, 138, 124, 152]

# ----------------------------------------------------------

# Classes and Objects

# class Person:
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age

#     def greet(self):
#        print(f"Hello, my name is {self.name}")

# ellie = Person("Ellie", 22)
# gabby = Person("Gabby", 23)

# ellie.greet() # output: Hello, my name is Ellie
# gabby.greet() # output: Hello, my name is Gabby

# ----------------------------------------------------------

# Functions
# def greetings():
#      print("Hello, World!")

# greetings() # output: Hello, World!

# ----------------------------------------------------------

# Modules

# import matplotlib.plotly as plt
# import random

# print(random.randint(1, 10))

# x = [1, 2, 3, 4, 5]
# y = [4, 6, 8]

# plt.plot(x, y)
# plt.show()

# ----------------------------------------------------------

# Parameters

# def add(x, y):
#   return x + y

# print(add(2, 3)) # output: 5
# print(add(21, 56)) # output: 77