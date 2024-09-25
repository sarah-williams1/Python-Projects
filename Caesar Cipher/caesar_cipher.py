"""
Thank you Al Sweigart (al@inventwithpython.com) for this project!
"""

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Encrypt letters by shifting them over a key number.")

# This section sets the stage for decrytion or encryption.
while True:
    print("Do you want to (e) encrypt or (d) decrpyt?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter either 'e' or 'd'. Thank you.")
    
 # Sets the key number for the Caesar Cipher
while True:
     max_key = len(symbols) - 1
     print("Please enter the key (0 to {}) to use.".format(max_key))
     response = input("> ").upper()
     if not response.isdecimal():
         continue
     if 0 <= int(response) < len(symbols):
         key = int(response)
         break

print("Enter the message to {}.".formate(mode))
message = input("> ")
translated_message = " "

# Encrypts or decrypts each symbol in the message
for symbol in message:
    if symbol in symbols:
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)
        translated_message = translated_message + symbols[num]
    else:
        translated_message = translated_message + symbol

print(translated_message)
        