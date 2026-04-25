# 3. Write a Python Program to get the largest and smallest number in a list without using built-in functions.
n = int(input("Enter the number of items: "))
a = [0] * n  
for i in range(n):
    a[i] = int(input("Enter number: "))

big = a[0]
small = a[0]

for b in a:
    if b > big:
        big = b
    if b < small:
        small = b

print("Largest:", big)
print("Smallest:", small)
