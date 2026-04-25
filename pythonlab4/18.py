# 18. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 15 (both included).
a = [b**2 for b in range(1, 16)]
print(a[:5] + a[-5:])
