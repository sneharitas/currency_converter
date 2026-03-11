"""TASK 1:
Program: Currency Input Program
Objective:
This program asks the user to enter a currency type and an amount.
It checks if the amount entered is a valid number.
Then it displays the currency and amount entered by the user.
"""

# Ask the user to enter the currency type
currency = input("Enter currency (USD or EUR): ")

# Ask the user to enter the amount
amount = input("Enter amount: ")

"""
Check if the amount entered by the user is a number.
If it is a number, convert it into float and print the result.
If it is not a number, show an error message.
"""

if amount.isdigit():
    amount = float(amount)

    print("Currency entered:", currency)
    print("Amount entered:", amount)

else:
    print("Invalid amount. Please enter a number.")
