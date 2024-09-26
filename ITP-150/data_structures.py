# strings
my_name = "Sarah"

# integers
my_age = 30

# floats
price = 4.75


# booleans
    # True or False
    # 1       0
is_cold = True
is_raining = 1

if is_cold:
    print("Wear a jacket")
if is_cold and is_raining:
    print("wear a jacket and bring an umbrella.\n\n\n\n\n")

# lists
    # Built in data type
    # Think of lists like a grocery list
items = [True, 1, 1.99, "Hello World", [1, 2, 3]]
print(items)

# For Loop
for item in items:
    print(item)
msg = items[3]
print(msg.upper())
print(msg[::-1])
    # slicing start: (to the left of the colon) stop: (in between the colons) step: -1 is starting at the end of a string
    # This will reverse a string
hello = msg[:5] # Go to message, start at index 0 and go up to index 5 but DO NOT include 5
print(hello)


# dictionaries
person = {"name": "Sarah", "age" : 30, "is_cold" : True}
    # Key built-in functions/ methods for dictionaries
    # .keys()
    # .values()
    # .items()

    # print the keys. 
print(person.keys())
for key in person.keys(): # This will return a list of keys, which means it is iterable
    print(key)
print(person.values())
for value in person.values():
    print(value)
# Printing the items (key-value)
for key, value in person.items():
    if key == "name":
        print(value.upper())
    else:
        print(f"{key} : {value}")
print("\n\n\n\n\n\n")

# TUPLES
my_tuple = (1, 2, 3, 4, 5)
my_other_tuple = ("yes", "no", "maybe")
print(my_tuple[1])
print(my_tuple[1:4]) # slices the tuple, just like a string. Starts at index 1 and goes up to index 4 (not includings index 4)

# SETS
my_set = {1, 2, 3, 4, 5, 6, 7, 8}
my_set_empty = {} # python will think this is a dictionary
my_set_empty_for_real = set()