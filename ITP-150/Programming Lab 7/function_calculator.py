"""
function_calculator.py
@author: Sarah Williams
Date: 15 October 2024
Assignment: Programming Lab 7 Function Calculator

Purpose: Use functions to perform mathematics
"""

def main():
    num1 = 10
    num2 = 3

    add_result = add_numbers(num1, num2)
    subtract_result = subtract_numbers(num1, num2)
    multiply_result = multiply_numbers(num1, num2)
    divide_result = divide_numbers(num1, num2)

    display_results(num1, "+", num2, "=", add_result)
    display_results(num1, "-", num2, "=", subtract_result)
    display_results(num1, "*", num2, "=", multiply_result)
    display_results(num1, "/", num2, "=", divide_result)

# Defining math functions (add, subtract, etc)
def add_numbers(mynum1, mynum2):
    my_add_result = 0
    my_add_result = mynum1 + mynum2
    return my_add_result
def subtract_numbers(mynum1, mynum2):
    my_subtract_result = 0
    my_subtract_result = mynum1 - mynum2
    return my_subtract_result
def multiply_numbers(mynum1, mynum2):
    my_multiply_result = 0
    my_multiply_result = mynum1 * mynum2
    return my_multiply_result
def divide_numbers(mynum1, mynum2):
    my_divide_result = mynum1 / mynum2
    return my_divide_result

def display_results(mynum1, operator, mynum2, equals, my_result):
    if type(my_result) == int:
        print(f"{mynum1}{operator}{mynum2}{equals}{my_result}")
    else:
        print(f"{mynum1}{operator}{mynum2}{equals}{my_result:.3f}")
        
# Calls main function
if __name__ == "__main__":
    main()