# %%

# Write a program that receives 4 heights using a loop
# and calculates the sum of these heights.

sum = 0
num_heights = 4 # Number of heights to be entered

for i in range(num_heights): # range(0, 4) -> 0, 1, 2, 3
    height = input("Enter a height in meters (e.g., 1.75): ")
    height = float(height)
    sum += height

print("The total sum of the heights is:", sum, "meters")