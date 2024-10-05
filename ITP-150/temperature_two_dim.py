"""
Author: Sarah Williams
Date: 05 October 2024
Assignment: Lab 5 Temperatures Two Dimensional List
"""

num_days = int(input("How many days do you want to track temperatures?\n "))
COLS = 4
sum_high_temps = 0
HIGH_TEMP = 90
temperatures = [[0 for col in range(COLS)] for row in range(num_days)]
print(temperatures)

for row in range(0, num_days, 1):
    temperatures[row][0] = input("Please enter the date: ")
    print(f"Please enter the low temperature for {temperatures[row][0]} : ")
    temperatures[row][1] = float(input())
    print(f"Please enter the high temperature for {temperatures[row][0]} : ")
    temperatures[row][2] = float(input())
    temperatures[row][3] = (temperatures[row][1] + temperatures[row][2]) / 2
print("-" * 50)

# Formatting the 2D List
print(f"{"Dates":12} {"Lows":<10} {"Highs":<10} {"Average Temps":<15}")
for row in range(0, num_days, 1):
    print(f"{temperatures[row][0]:<10s} {temperatures[row][1]:<10.1f} {temperatures[row][2]:<10.1f} {temperatures[row][2]:<10.1f} {temperatures[row][3]:<10.1f}")
print("-" * 50)

# Finding the lowest temperature and its date
lowest_low = temperatures[0][1]
lowest_low_date = temperatures[0][0]
for row in range(0, num_days, 1):
    if temperatures[row][1] < lowest_low:
        lowest_low = temperatures[row][1]
        lowest_low_date = temperatures[row][0]
print(f"{"Lowest Low":30s} {lowest_low:>12.1f}")
print(f"{"Lowest Low Date":30s} {lowest_low_date:>12s}")

# Finding the highest temperature and its date
highest_high = temperatures[0][2]
highest_high_date = temperatures[0][0]
for row in range(0, num_days, 1):
    if temperatures[row][2] > highest_high:
        highest_high = temperatures[row][2]
        highest_high_date = temperatures[row][0]
print(f"{"Highest High":30s} {highest_high:>12.1f}")
print(f"{"Highest High Date":30s} {highest_high_date:>12s}")

# Calculate and print average highs
for row in range(0, num_days, 1):
    sum_high_temps = sum_high_temps + temperatures[row][2]
average_highs = sum_high_temps / num_days
print(f"{"Average Highs":30s} {average_highs:>12.1f}")
for row in range(0, num_days, 1):
    if temperatures[row][2] >= HIGH_TEMP:
        print("The average temp exceeded ", HIGH_TEMP, " on ", temperatures[row][0], " recorded at ",
              temperatures[row][2], ".")
print("-" * 50)
