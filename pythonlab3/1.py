# 1. Write a Python program to find the sum of n natural numbers.
a = int(input("Enter a number: "))
b = 0
for c in range(1, a + 1):
    b += c
print("Sum is:", b)
