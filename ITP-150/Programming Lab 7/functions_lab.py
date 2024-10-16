"""
 functions_lab.py
 @author: Sarah Williams
 Date: 15 October 2024
 Assignment: Lab 7 Functions Lab
"""

import random

print("\nTask 1: Import a function.")
integer = random.randint(0, 100)
print("A random int between 0 and 100 is: ", integer)

print("\nTask 2: See the help.")
print("If youw ant to see a function's documentation, enter ")
print("help followed by the function name.")

print("\nTask 3: Basic function without parameters and arguments.")
def my_function():
    location = "We are inside of my function."
    print(location)

print("Before calling my_function: ")
my_function()
print("After calling my_function: ")

print("\nTask 4: Basic function that has a docstring and the keyword pass.")
def my_empty_function():
    """ This function is empty but has this line of documentation."""
my_empty_function
help(my_empty_function)

print("\nTask 5: Positional arguments require same qty of arguments and" 
     " parameters in teh same order representing the same data types.")
def water(qty, h2o, price):
    print(f"{qty} {h2o} cost {price:.2f}")
print("Call 1: ")
water(1, "Aquafina", 2.69)
print("Call 2 throws an error because we passed only 2 arguments.")
# water(1, "Dasani")
print("Call 3 does not throw an error but is logically incorrect.")
water("Nestle Pure Water", 2.69, 1)

print("\nTask 6: Keyword arguments allow flexibility.")
def water_keywords(qty, h2o, price):
    print(f"{qty} {h2o} cost ${price:.2f}")
print("Call 1: You must supply the parameters.")
# water_keywords()
print("\nCall 2: Keyword argments in the same order as the function def.")
water_keywords(qty=2, h2o="Aquafina", price=2.69)
print("\nCall 3: Keyword arguments NOT in the order of the function def.")
water_keywords(h2o="Aquafina", price=2.69, qty=2)
print("Takeaway: Using keyword arguments allows us to pass in different order.")
print("\nCall 4: Can we leave out an argument using keyword arguments? NO.")
# water_keywords(h2o="Aquafina", price=2.69)
print("\nCall 5: Try a mix of positional and keyword arguments.")
water_keywords(2, h2o="Aquafina", price=2.69)
print("Positional arguments must come before keyword arguments.")
print("\nCall 6: Keyword args cannot follow positional args.")
# water_keywords(qty=2, "Aquafina", price=2.69)
print("\nCall 7: Can you change the keyword argument name? NO!")
# water_keywords(qty=2, brand="Aquafina", price= 2.69)

print("\nTask 7: Default parameters allow us to set default values for")
print("a parameter in the function definition.")
def water_default(qty=1, h2o="Aquafina", price=2.69):
    print(f"{qty} {h2o} cost ${price}")

print("\nCall 1: Sending different arguments than the default.")
water_default(2, "Dasani", 3.50)
print("Takeaway is that if you send different arguments up when")
print("calling a function with default parameters, your arguments")
print("will override the defaults which is a good thing.")
print("\nCall 2. Sending up 2 arguments to see the default come into play.")
water_default(2, "Dasani")
print("Takeaway is that you no longer have to supply all three arguments")
print("if default parameters have been specified in the function definition.")
print("\nCall 3: Experiment using position and keyword arguments on a function with default parameters.")
# water_default(2, h2o="Dasani", 3.50)
print("Takeaway is that you can use positional and keyword arguments")
print("with a function that has default parameters but you still must")
print("follow the rule that positional arguments must come before keyword arguments.")

print("\nTask 8: *args (Argument Tuple Packing)")
print("You can use argument tuple packing when you don't know how many arguments you need.")
def args_function(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)
args_function(2, 4, 6, 8, 10)

print("\nTask 9: Practical example of *args")
def avg_args(*args):
    sum_args = 0
    for i in args:
        sum_args = sum_args + 1
        return sum_args / len(args)
print(avg_args(2, 4, 6, 8, 10))
print(avg_args(1, 3, 5))

print("\nTask 10: Argument tuple unpacking.")
print("This works with tuples, lists, and sets. Example is a tuple.")
def unpack_args(a, b, c):
    print("a is ", a)
    print("b is ", b)
    print("c is ", c)
stuff = (1, "Perrier", 5.00)
print(type(stuff))
unpack_args(*stuff)

print("\nTask 11: Argument tuple packing and unpacking.")
print("This works with tuples, lists, and sets. Example is a tuple.")
def packing(*args):
    print(type(args), args)
stuff = (1, "Perrier", 5.00)
packing(*stuff)

print("\nTask 12: Arbitrary keyword arguments, **kwargs'")
print("If you do not know how many keyword arguments that will be passed into\
 your function, add two asterisks: ** before the parameter name in the\
 function definition.")
def pets_function(**pets):
    print("My dog's name is " + pets["dog"])
    print("My cat's name is " + pets["cat"])
pets_function(cat = "Miss Kitty", dog = "Buddy")
