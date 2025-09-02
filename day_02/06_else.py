# %%
print("How old are you?")

age = int(input())
if age >= 70:
    print("You are a senior citizen. Take care!")

elif age >= 18:
    print("You can drink alcohol.")

elif age == 17:
    print("You are almost an adult. Get some soda.")

else:
    print("You cannot drink alcohol.")