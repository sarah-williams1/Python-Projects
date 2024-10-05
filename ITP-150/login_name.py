"""
Author: Sarah Williams
Date: 05 October 2024
Assignment: Lab 4 Login Name
"""

import random

first_name = input("Enter your first name.\n")
middle_name = input("Enter your middle name.\n")
last_name = input("Enter your last name.\n")
id_number = random.randint(0, 100)

print("Your system login name is...")
set1 = first_name[0 : 1]
set2 = middle_name[0 : 1]
set3 = last_name[0 : 1]
login_name = set1.lower() + set2.lower() + set3.lower() + str(id_number)
print(login_name)

is_valid = False

while is_valid == False: 
    correct_length = False
    check_uppercase = False
    check_lowercase = False
    check_number = False

    print("Please enter your password.\n"
          "It must contain at least 8 characters.\n"
          "It must contain at least 1 lowercase letter.\n" 
          "It must contain at least 1 uppercase letter.\n"
          "It must contain at least 1 number.")
    password = input("Please enter your password now: \n")
    if len(password) >= 8:
        correct_length = True
    for char in password:
        if char.isupper():
            check_uppercase = True
        if char.islower():
            check_lowercase = True
        if char.isdigit():
            check_number = True
    if correct_length and check_number and check_lowercase and check_uppercase:
        print("The passowrd is value.")
        is_valid = True
    else: 
        is_valid = False
        print("Invalid password.")
        if not correct_length:
            print("Your password does not have 8 characters.")
        if not check_lowercase:
            print("Your password does not have a lowercase letter.")
        if not check_number:
            print("Your password does not have a number.")
        if not check_uppercase:
            print("Your password does not have an uppercase letter.")
            
print("Your username is ", login_name)
print("Your password is ", password)