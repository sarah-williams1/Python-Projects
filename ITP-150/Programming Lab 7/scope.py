"""
scope.py
@author: Sarah Williams
Date: 15 October 2024
Assignment: Lab 7 Scope

"""

x = 7

def main():
    access_global()
    try_to_modify_global()
    print("x printed after try_to_modify_global is", x)
    modify_global()
    print("x printed after modify_global", x)
    try_to_modify_global()

def access_global():
    print("x printed from access_global", x)
def try_to_modify_global():
    x = 3.5
    print("x printed from try_to_modify_global", x)
def modify_global():
    global x
    x = "Hello"
    print("x printed from modify global: ", x)
if __name__ == "__main__":
    main()