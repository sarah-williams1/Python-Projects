"""
seconds_converter.py
@Author: Sarah Williams
Created: 26 August 2024

This script will prompt the user to input a number of seconds, then it calculates and displays the hours, minutes, and seconds for the number of seconds input.

"""
# doing a division operation with // will get rid of the decimal ending, leaving just a whole
total_seconds = int(input("Enter a number of seconds: \n"))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60

print('Hours:   ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)
