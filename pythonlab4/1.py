# 1. Write a Python Program to print all the items in a list.
a = int(input("Enter the number of items: "))
lst = [None] * a
for b in range(a):
    lst[b] = input("Enter item: ")

for b in lst:
    print(b)

