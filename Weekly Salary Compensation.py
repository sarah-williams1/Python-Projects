'''
Assignment: Weekly Salary Compensation
Author: Sarah Williams
Created: 31 August 2024

Enter from the keyboard two values:
Number of hours you worked during a week and hourly rate as a dollar amount (do not use $ in entry though)
The program will calculate the total compensation and will display the result in the following form:
Your total compensation for a week is $ 670, where 670 is a calculated Number
and will depend on the initial data that you enter

'''

hours_worked = 40
weekly_compensation = 670
hourly_rate = weekly_compensation / hours_worked

print("I worked " + str(hours_worked) + "hours this week.")
print("My hourly rate is $" + str(hourly_rate) + " which gave me a weekly compensation of $" + str(weekly_compensation))

