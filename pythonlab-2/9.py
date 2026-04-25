# 9. Write a Python script that takes two numbers as input and prints their sum, difference, product, 
# and quotient using match case.
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
match "do":
    case "do":
        print("Sum:", m + n)
        print("Diff:", m - n)
        print("Product:", m * n)
        if n != 0:
            print("Quotient:", m / n)
        else:
            print("Cannot divide by zero")