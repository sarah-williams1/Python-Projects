"""
Author: Sarah Williams
Date: 12 October 2024

Purpose: Create a file. 
"""


def main():
    outfile = open("philosophers.txt", "w")

    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    outfile.write("This file was created with the python file named 'file_practice.py'. ")

    outfile.close()
main()