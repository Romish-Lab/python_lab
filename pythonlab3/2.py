# 2. Write a program to read an integer from user. For all numbers except those divisible by 10, print them.
a = int(input("Enter a number: "))
for b in range(1, a + 1):
    if b % 10!= 0:print(b, end=" ")
