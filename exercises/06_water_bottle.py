# Make a program that sells a bottle of water:
# If the customer chooses natural mineral water, it will cost R$1.50
# If the customer chooses sparkling mineral water, it will cost R$2.50

text = """
What type of water do you want?
(1) Natural mineral water - R$1.50
(2) Sparkling mineral water - R$2.50
"""

option = input(text)

if option == "1":
    print("You chose natural mineral water. The price is R$1.50")
elif option == "2":
    print("You chose sparkling mineral water. The price is R$2.50")   
else:
    print("Invalid option. Please choose 1 or 2.")
