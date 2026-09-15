# This is simple bill calculator
price = float(input("How much does sandal cost in Ksh? "))
quantity = int(input("How many pair of sandal do you want to buy? "))
total = price * quantity
print(f"The price of sandal is Ksh {price:.2f}")
print(f"The pair of sandal you want to buy is {quantity}")
print(f"The total price of the sandal is Ksh {total:.2f}")
