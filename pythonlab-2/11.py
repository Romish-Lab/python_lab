# 11. Create a Python script that converts temperature from Fahrenheit to Celsius and vice versa, 
# based on user input.
temp = float(input("Enter temperature: "))
scale = input("Is it in (C)elsius or (F)ahrenheit? ").lower()
if scale == 'c':
    print("In Fahrenheit:", (temp * 9/5) + 32)
elif scale == 'f':
    print("In Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid input")