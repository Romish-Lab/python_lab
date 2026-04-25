# 6. Write a Python script that takes two numbers as input and prints their sum, difference, product, and quotient.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", x + y)
print("Diff:", x - y)
print("Product:", x * y)
if y != 0:
    print("Quotient:", x / y)
else:
    print("Cannot divide by zero")