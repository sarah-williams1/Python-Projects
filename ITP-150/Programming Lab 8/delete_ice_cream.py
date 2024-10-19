"""
delete_ice_cream.py
@author: Sarah Williams
Date: 19 October 2024
"""
import os

def main():
    found = False
    try:
        search = input("Enter an ice cream flavor to search for: ")
        ice_cream_file = open("ice_cream.txt", "r")
        temp_file = open("temp.txt", "w")
        descr = ice_cream_file.readline()

        while descr != "":
            quarts = int(ice_cream_file.readline())
            descr = descr.rstrip("\n")
            if descr != search:
                temp_file.write(descr + "\n")
                temp_file.write(str(quarts) + "\n")
            else:
                found = True
            descr = ice_cream_file.readline()
        ice_cream_file.close()
        temp_file.close()
        os.remove("ice_cream.txt")
        os.rename("temp.txt", "ice_cream.txt")

        if found:
            print("The ice_cream.txt file has been updated.")
        else:
            print("That ice cream flavor was not found in the file.")
    except IOError:
        print("An error occurred trying to read the file.")
    except Exception as err:
        print("An error occurred.", err)

main()