"""
Author: Sarah Williams
Date: 12 October 2024

Purpose: Create a file and stuff.
"""


def main():
    # Writing a file.
    outfile = open("philosophers.txt", "w")

    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n\n")

    outfile.write("This file was created with the python file named 'file_practice.py'. ")

    outfile.close()
    print("Data written to philosophers.txt")

    # Creating a file where the user has to input numbers.
    # Specified a file path for the numbers.txt file to be saved to.
    # Default file path was the main Python-Projects folder.
    outfile = open("ITP-150//File Writing Practice//numbers.txt", "w")
    # Get three numbers from the user.
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))
    # Write the numbers to the file.
    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")
    # Close the file.
    outfile.close()
    print("Data written to numbers.txt")
main()

def readfile():
    infile = open("philosophers.txt", "r")
    # Read three lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    # Closes the file.
    infile.close()
