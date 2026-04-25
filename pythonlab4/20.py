# 20. Write a Python program to insert n values in a list and find those values in a list that are greater than a specified number.
a = [1, 2, 3, 4, 5]
n = 3
b = [c for c in a if c > n]
print(b)
