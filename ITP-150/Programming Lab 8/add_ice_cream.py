"""
add_icecream.py
@author: Sarah Williams
Date: 19 October 2024
Assignment: Programming Lab 8 Add Icecream

Purpose: Create a file called ice_cream.txt and write data to it using the IO library.
"""

def main():
    try:
        run_program = "y"
        print("Let's update the ice cream inventory!")
        while run_program.lower() == "y":
            with open("ice_cream.txt", mode="a") as ice_cream_file:
                ice_cream = input_ice_cream()
                quarts = input_quarts()
                ice_cream_file.write(ice_cream + "\n")
                ice_cream_file.write(str(quarts) + "\n")
                print("Do you want to add another record?")
                run_program = input("Y = Yes, anything else is No.\n")
    except IOError:
        print("The file could not be found or accessed.")
    except Exception as err:
        print("An error has occurred: ", err)

def input_ice_cream():
    ice_cream = input("Enter the flavor of ice cream:\n")
    return ice_cream

def input_quarts():
    while True:
        try:
            quarts = int(input("Enter the quarts: "))
            if quarts < 0:
                raise Exception
            else:
                return quarts
        except ValueError:
            print("Invalid. You must enter an integer >= 0:\n")
        except Exception:
            print("Invalid. Enter a value >= 0:\n")

if __name__ == "__main__":
    main()