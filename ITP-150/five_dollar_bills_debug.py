"""
Created on Tue Sep 14 21:29:26 2021
five_dollar_bills_debug.py
@author: put your name here
"""

print("This program makes change in $5 increments. It can only dispense $5 evenly with no remainder. 3 attempts max.")
print("Example: Entering $15 will get you (3) $5 bills.")
print("Example: Entering $12 will result in 'Error'.")


def change_amount():
    amount = int(input("Enter amount you need change for: \n"))
    counter = 3
    if amount % 5 == 0:
        print(f"You will get {amount/5} $5.00 bills in change. Thank you for making change!")
    else:
        error = "Invalid entry. Amount must be divisible by 5."
        counter -= 1
        print(error)
        print(f"{counter} tries remaining.")
    if counter == 0:
        return

def main():

    print("This program makes change in $5 increments. It can only dispense $5 evenly with no remainder. 3 attempts max.")
    print("Example: Entering $15 will get you (3) $5 bills.")
    print("Example: Entering $12 will result in 'Error'.")
    
change_amount()