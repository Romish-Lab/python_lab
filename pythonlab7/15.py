# 15. Write a Python recursive function to find out factorial of any given number.
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
num = 5
print(f"Factorial is {fact(num)}")
