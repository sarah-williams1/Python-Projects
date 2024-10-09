"""
Created on Tue Sep 14 21:29:26 2021
five_dollar_bills_debug.py
@author: put your name here
"""
"""
Requirements:
This program makes change in 5$ bills. US Currency.
It can only dispense 5$ bills thus a valid
amount must divide evenly by 5 with no remainder.
FYI the if statement for detecting a multiple of 5
for a variable named amount is
if amount % 5 == 0:
The user gets 3 attempts at entering a value that will divide evenly
into 5$ bills.
If the user enters a valid amount, then the
program displays the quantity of 5$ bills and
breaks out of the loop as shown in the test cases
below where 15.00 is used as the amount to change into 5$ bills:
How to test for a valid amount:
This program will make change in 5 dollar bills for an amount given.
You are allowed 3 tries to enter an amount evenly divisible by 5.
Attempt 1 : Please enter a value to change into 5 dollar bills:
As an example, for $15.00, enter 15.00.
15.00
You can have (3) 5$ dollar bill(s)!
Thanks for making change!
How to test for invalid amounts. Notice in the
following test case, the user makes 2 attempts which
are invalid (12.00, 11.00) before entering a valid
amount on the 3rd try which is 10.00.
This program will make change in 5 dollar bills for an amount given.
You are allowed 3 tries to enter an amount evenly divisible by 5.
Attempt 1 : Please enter a value to change into 5 dollar bills:
As an example, for $15.00, enter 15.00.
12.00
Invalid. 2 more attempt(s)!
12.00 will not divide evenly into 5$ bills
Attempt 2 : Please enter a value to change into 5 dollar bills:
As an example, for $15.00, enter 15.00.
11.00
Invalid. 1 more attempt(s)!
11.00 will not divide evenly into 5$ bills
Attempt 3 : Please enter a value to change into 5 dollar bills:
As an example, for $15.00, enter 15.00.
10.00
You can have (2) 5$ dollar bill(s)!
Thanks for making change!
"""
\
    
    
    
    