# 8. Write a Python program to calculate the average value of numbers in a tuple of tuples.
a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
b = [sum(x)/len(x) for x in a]
print(b)

c = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
d = [sum(x)/len(x) for x in c]
print(d)
