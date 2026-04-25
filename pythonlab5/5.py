# Program to sort a tuple by its float element using loop.
a = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
a = list(a)  

n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if float(a[j][1]) < float(a[j+1][1]):   
            a[j], a[j+1] = a[j+1], a[j]        

print(a)
