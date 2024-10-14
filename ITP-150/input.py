# input.py
# Author: Sarah Williams
# Created: 26 August 2024

name = input("What is your name?\n")
age = int(input("What is your age?\n"))
income = float(input("How much money do you want to make?\n"))

print("Name: ", name)
print("Age: ", age)
# print("Income: ", income)
print("Income: ", format(income, ',.2f'))
