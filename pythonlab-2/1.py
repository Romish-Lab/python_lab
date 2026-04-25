# 1. Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.
num1 = int(input("Enter a number: "))
if num1 > 17:
    print((num1 - 17) * 2)
else:
    print(17 - num1)