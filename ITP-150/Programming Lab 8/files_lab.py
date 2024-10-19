"""
files_lab.py
@author: Sarah Williams
Date: 19 October 2024
Assignment: Programming Lab 8 Files Lab
"""

import csv

print("Task 1: Create a text file and write to it.")
# Creating a file by writing to it.
# With statement acquires a resource which is called "accounts"
# io.TextIOWrapper and when done, with automatically closes resources

try:
    with open("accounts.txt", mode="w") as accounts:
        accounts.write("100 Jones 24.98\n")
        accounts.write("200 Doe 345.67\n")
        accounts.write("300 White 0.00\n")
        accounts.write("400 Stone -42.16\n")
        accounts.write("500 Rich 224.62\n")
    print(id(accounts))
    print(type(accounts))
except IOError:
    print("Well hmm...File not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("\nTask 2: Open the file we just created and printing out its contents.")
try:
    with open("accounts.txt", mode="r") as accounts:
        print(f"{"Accounts":<10} {"Name":<10} {"Balance":>10}")
        for record in accounts:
            account, name, balance = record.split()
            print(f"{account:<10} {name:<10} {balance:>10}")
except IOError:
    print("Well hmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("\nTask 3: Read the accounts.txt file")
try:
    my_account = open("accounts.txt", "r")
    print(my_account.read())
    my_account.close()
except IOError:
    print("Well hmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("Task 4: Read the first 3 characters(bytes) from the accounts.txt file.")
try:
    my_account = open("accounts.txt", "r")
    print(my_account.read(3))
    my_account.close()
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("\nTask 5: Readline")
try:
    my_account = open("accounts.txt", "r")
    print(my_account.readline())
    print(my_account.readline(3))
    my_account.close()
except IOError:
    print("Well hmmm...file not found or path is incorrect")
except Exception as err:
    print("An error occurred: ", err)

print("Task 6: Use a for loop to read the file line by line.")
try: 
    my_account = open("accounts.txt", "r")
    for line in my_account:
        print(line)
    my_account.close()
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("Task 7: Using with and for to read and print.")
try:
    with open("accounts.txt", mode="r") as reader:
        for line in reader:
            print(line, end="")
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("\nTask 8: Use writer to write the accounts file in reversed order to accounts_reversed.txt")
print("Use the reader.readlines() method to read the file then you can reverse\
      it with writelines(reversed())")
try:
    with open("accounts.txt", "r") as reader:
        accounts = reader.readlines()
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error as occurred: ", err)
try:
    with open("accounts_reversed.txt", "w") as writer:
        writer.writelines(reversed(accounts))
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("\nTask 9: Open the accounts_reversed.txt file and read it\
      and print its contents.")
try:
    with open("accounts_reversed.txt", "r") as reader:
        for line in reader:
            print(line, end="")
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)

print("\nTask 10: Open the accounts_headings.csv file and print its\
 contents including the headings.")
try:
    with open("accounts_headings.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f"Column names are {", ".join(row)}")
                print(f"{row[0]:<12} {row[1]:>10} {row[2]:>10}")
                line_count = line_count + 1
            else:
                print(f"{row[0]:<12} {row[1]:>10} {row[2]:>10}")
                line_count = line_count + 1
        print(f"Processed {line_count} lines.")
except IOError:
    print("Well hmmm...file not found or path is incorrect.")
except Exception as err:
    print("An error occurred: ", err)