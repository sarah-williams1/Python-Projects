""" 
sale_price.py
@author: sarah williams
Created: 26 August 2024

""" 

regular_price = float(input("Please enter the regular price: "))
print("Please enter the discount percent (ex: 10 for 10%): ")
discount_percent = float(input())
discount_amount = regular_price * discount_percent / 100
sale_price = regular_price - discount_amount

print("Regular Price: ", format(regular_price, ',.2f'))
print("Discount Amount: ", format(discount_amount, ',.2f'))
print("Sale Price: ", format(sale_price, ',.2f'), sep=' $', end='')
print("\n Thank you for your business!")
