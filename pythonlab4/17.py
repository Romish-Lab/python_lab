# 17. Write a Python Program to sort a list of lists by a given index of the inner list.
a = [[1, 3], [3, 2], [2, 1]]
a.sort(key=lambda x: x[1])
print(a)
