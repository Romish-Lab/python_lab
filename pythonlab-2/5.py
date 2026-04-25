# 5. Write a Python program to check whether a variable is an integer, or string, or a list, or tuple, or set.
val = [1, "text", [1,2], (3,4), {5,6}]
for i in val:
    print(i, "is type", type(i))