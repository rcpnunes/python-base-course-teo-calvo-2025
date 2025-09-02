# Change the previous program to consider the number of water bottles

text = """
What type of water do you want?
(1) Natural mineral water - R$1.50
(2) Sparkling mineral water - R$2.50
"""

option = input(text)

item_value = 0

if option == "1":
    item_value = 1.50
elif option == "2":
    item_value = 2.50  
if item_value == 0:
    print("Invalid option. Please choose 1 or 2.")
else:
    volume = input("How many bottles do you want? ")
    volume = int(volume)
    total = item_value * volume
    print("The total price is R$", total)