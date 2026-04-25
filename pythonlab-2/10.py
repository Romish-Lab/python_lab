# 10. Write a script that asks the user for their name and age, then prints a message that tells them 
# the year in which they will turn 100 years old.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year_100 = 2025 + (100 - age)
print(name + ", you will turn 100 years old in the year", year_100)