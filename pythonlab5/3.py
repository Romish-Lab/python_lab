#write a python program to find repeated item in a tuple
a = (1, 2, 3, 2, 4, 5, 2, 6)

count = {}
for x in a:
    if x in count:
        count[x] += 1  
    else:
        count[x] = 1    

for k in count:
    if count[k] > 1:
        print(k)
