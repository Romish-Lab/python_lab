# 8. Write a Python program that accepts a string and calculates the number of letters and digits.
a = input("Enter a string")
b = c = 0
for d in a:
    if d.isalpha():
        b += 1
    elif d.isdigit():
        c += 1
print("Letters", b)
print("Digits", c)
