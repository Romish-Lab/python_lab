# 4. Write a Python program to get the Fibonacci series up to a given number.
a = int(input("Enter limit: "))
b, c = 0, 1
while b <= a:
    print(b, end=' ')
    b, c = c, b + c
