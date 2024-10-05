"""
Author: Sarah Williams
Date: 05 October 2024
Assignment: Lab 5 Temperatures

Purpose: Track Temperature over a number of days then calculate the min, max, and average for the Temperatures entered.
"""

num_days = int(input("How many days do you want to track?\n"))
dates = [" "] * num_days
lows = [0.0] * num_days
highs = [0.0] * num_days
average_temp = [0.0] * num_days

for i in range(0, num_days, 1):
    dates[i] = input("Please enter the date (ex. Oct. 9)")
    print("Pleaes enter the low for ", dates[i])
    lows[i] = float(input())
    print("Please enter the highs for ", dates[i])
    highs[i] = float(input())
    average_temp[i] = (lows[i] + highs[i]) / 2

print("-" * 51)
print(f"{"Dates":8} {"Lows":>10s} {"Highs":>10s} {"Average Temp":>20s}")
for i in range(0, len(dates), 1):
    print(f"{dates[i]:8} {lows[i]:10.1f} {highs[i]:10.1f} {average_temp[i]:20.1f}")
print("-" * 51)

minimum_temp = min(lows)
minimum_temp_date = " "
for i in range (0, len(lows), 1):
    if lows[i] == minimum_temp:
        minimum_temp_date = dates[i]
print("-" * 51)
print(f"{"Lowest Temperature":30} {minimum_temp:20,.1f}")
print(f"{"Lowest Temperature Date":30} {minimum_temp_date:>20s}")

maximum_temp = max(highs)
maximum_temp_date = " "
for i in range (0, len(highs), 1):
    if highs[i] == maximum_temp:
        maximum_temp_date = dates[i]
print("-" * 51)
print(f"{"Highest Temperature":30} {maximum_temp:20,.1f}")
print(f"{"Maximum Temp Date":30} {maximum_temp_date:>20s}")

sum_average_temps = sum(average_temp)
average_average_temp = sum_average_temps / len(average_temp)

print("-" * 51)
print(f"{"Average Temperature":30} {average_average_temp:20,.1f}")
print("-" * 51)