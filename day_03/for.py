# %%
name = "Teodoro Calvo"

for letter in name:
    print(letter)

# %%
# Multiplication table of 2
number = 2
max_count = 100

for i in range(1,max_count + 1):
    print(number, "x", i, "=", number * i)

# %%
# Witch numbers can be divided by 4?

for i in range (4, 101):
    if i % 4 == 0:
        print(i, "is divisible by 4")    