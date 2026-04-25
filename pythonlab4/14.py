# 14. Write a Python program to sort a given list of strings (numbers) numerically.
a = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
a = [int(b) for b in a]
a.sort()
print(a)
