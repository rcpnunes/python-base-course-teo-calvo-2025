# %%

# Witch numbers can be divided by 4?

count = 4

while count <= 100:
    rest = count % 4
    if rest == 0:
        print(count, "is divisible by 4")

    count += 1 # count = count + 1    