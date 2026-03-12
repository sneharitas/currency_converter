"""
Author: Sneha Shrestha
Date: 11th March,2026
Task 4: Print conversion history report 
Description:  Display a formatted conversion report including user name, USD, and NPR.
 Focus: output formatting, syntax.
Implementation Details: 

Output / Formatting:
1. Store each transaction result.
2. After loop finishes, print conversion history.
3. Display transaction number, currency type, amount, and converted NPR.
4. The program prints a conversion report using print() and f-strings which allows to insert the variables directly inside the string.
5. The report includes the user’s name, amount in USD, and converted amount in NPR.
6. Optional formatting like .2f or commas can be used to display numbers neatly with two decimal places and thousands separators.
7. History.append() adds the transaction values to the list so we can print it all later
8. enumerate(history, 1) gives a number (i) starting from 1 for each transaction.
9. currency, amount, npr = record unpacks the tuple into variables.
10. Prints the transaction in a readable format.

 #step 1: creates an empty list to store the conversion history
history = []

#step 2: Take all the transaction calculation from my collaborators

#step 3: Take the convert amount to NPR based on currency

#step 4: Store all the transaction on the history list 

history.append ((Username, Currency.upper(), Amount, npr)) 

#step 5: Print the conversion history report
print("\n==============Conversion History Report==================")
for i, record in enumerate(history, 1):
   Username, Currency, Amount, NPR = record
   print(f"{Username} Transaction {i}: {Currency} {Amount} -> NPR"{npr}")
print ("==========================================================")
"""

"""TASK 1:
Program: Currency Input Program
Objective:
This program asks the user to enter a currency type and an amount.
It checks if the amount entered is a valid number.
Then it displays the currency and amount entered by the user.
"""
transactions = []

for i in range(4):

    currency = input("Enter currency (USD or EUR or JPY or GBP): ")
    amount = float(input("Enter amount: "))

    print("Currency entered:", currency)
    print("Amount entered:", amount)

    if currency == "USD":
        converted_amount = amount * 132
    elif currency == "EUR":
        converted_amount = amount * 145
    elif currency == "JPY":
        converted_amount = amount * 9.4
    elif currency == "GBP":
        converted_amount = amount * 198
    else:
        print("Unsupported currency. Conversion not possible.")
        exit()

    print("Converted amount in NPR:", converted_amount)

    transactions.append((currency, amount, converted_amount))


print("\n======== Conversion History Report ========")

for i, transaction in enumerate(transactions, start=1):
    currency, amount, converted_amount = transaction
    print(f"Transaction {i}: {currency} {amount} -> NPR {converted_amount}")
