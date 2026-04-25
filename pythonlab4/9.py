# 9. Write a Python Program to print a specified list after removing the 0th, 4th and 5th element.
a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in sorted([0, 4, 5], reverse=True):
    del a[i]
print(a)
