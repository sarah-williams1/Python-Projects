"""
Author: Sarah Williams
Date: 05 October 2024
Assignment: Lab 4: Sentinel Value Loop

"""

grand_total = 0
run_program = input("Please enter Yes to run the program or No to quit.\n")
while run_program.lower() == "yes":
    max_num = 5
    total = 0
    print("This program calculates the sum of ", max_num, "numbers.")

    for counter in range(0, max_num, 1):
        print("---------Number", (counter + 1), "----------")
        number = int(input("Enter a whole number: "))
        total = total + number
    print("The total for just this set of numbers is ", total)
    grand_total = grand_total + total
    print("Please enter Yes to run the program again or No to quit.\n")

print("The grand total for all sets of numbers is ", grand_total)