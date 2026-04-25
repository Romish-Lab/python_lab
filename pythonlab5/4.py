# Program to replace the last value of tuples in a list
a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
b = []
for x in a:
    temp = list(x)         
    temp[-1] = 100         
    b.append(tuple(temp))  
print(b)
