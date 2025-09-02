# Write a program that receives an indefinite number of values corresponding to "account balance",
# but when the user presses "enter" without typing any value, the program stops
# receiving values and displays the sum of all previously entered values.


total_balance = 0

while True:
    balance = input("Enter your account balance (or press Enter to finish): ")
    if balance == "":
        break

    total_balance += float(balance)

print("The total account balance is: R$", total_balance)