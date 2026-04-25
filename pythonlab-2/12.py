# 12. Create a program that asks for an age and prints “Child” if the age is less than 13, 
# “Teenager” if the age is between 13 and 19, and “Adult” for ages 20 and above.
age2 = int(input("Enter your age: "))
if age2 < 13:
    print("Child")
elif age2 < 20:
    print("Teenager")
else:
    print("Adult")