"""
search_ice_cream.py
@author: Sarah Williams
Date: 19 October 2024
Assignment: Programming Lab 8 Search Ice Cream

Purpose: Search the ice_cream.txt file for items entered in it.
"""

def main():
    found = False
    try:
        ice_cream = input("Enter an ice cream flavor to search for: ")
        ice_cream_file = open("ice_cream.txt", "r")
        descr = ice_cream_file.readline()

        while descr != "":
            quarts = int(ice_cream_file.readline())
            descr = descr.rstrip("\n")
            if descr == ice_cream:
                print("Ice Cream: ", descr)
                print("Quarts: ", quarts)
                print()
                found = True
            descr = ice_cream_file.readline()
        ice_cream_file.close()
        if not found:
            print("That item was not found in the file.")
    except IOError:
        print("An error occurred trying to read the file.")
    except Exception as err: 
        print("An error occurred: ", err)
        
if __name__ == "__main__":
    main()