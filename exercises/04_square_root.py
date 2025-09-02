# Make a program that receives an integer
# and calculates its square root and displays the result.

number = input("Enter an integer to find its square root: ")
number = int(number)
square_root = number ** 0.5
square_root = round(square_root, 2)

print("The square root of", number, "is", square_root)