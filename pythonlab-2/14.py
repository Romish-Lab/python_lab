# 14. Write a Python program that takes a number and prints whether it is “Even”, “Odd”, “Zero”, or 
# “Invalid” for non-integer inputs. This program should first check if the input is a valid integer 
# and then check for the other conditions.
val2 = input("Enter a number: ")
if val2.isdigit():
    val2 = int(val2)
    if val2 == 0:
        print("Zero")
    elif val2 % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid")