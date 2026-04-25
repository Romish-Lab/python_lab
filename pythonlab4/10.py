# 10. Write a Python Program to check if each number is prime in a given list of numbers.
a = [3, 4, 5, 10, 13]
for b in a:
        for c in range(2, b):
            if b % c == 0:
                break
        else:
            print(b, "is prime")
