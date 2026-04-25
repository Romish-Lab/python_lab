# Program to convert a tuple of positive integers into an integer
a = (1, 2, 3)

num = ""
for x in a:
    num += str(x)   
b = int(num)
print(b)
