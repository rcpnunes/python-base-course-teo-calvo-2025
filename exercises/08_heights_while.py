# Write a program that receives 4 heights using a loop
# and calculates the sum of these heights.

sum = 0
num_heights = 4

while num_heights > 0:
    height = input("Enter a height in meters (e.g., 1.75): ")
    height = float(height)
    sum += height
    num_heights -= 1  # num_heights = num_heights - 1

print("The total sum of the heights is:", sum, "meters")