# Question 6: Check variable type (int, str, float)
my_var =  (input("Enter any number"))

if isinstance(my_var, int):
    print(f"The variable is an integer.")
elif isinstance(my_var, str):
    print(f"The variable is a string.")
elif isinstance(my_var, float):
    print(f"The variable is a float.")
else:
    print(f"The variable is not an integer, string, or float.")