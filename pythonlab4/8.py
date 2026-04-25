# 8. Write a Python program to print the numbers of a specified list after removing even numbers from it.
a = [1, 2, 3, 4, 5, 6]
b=[]
for i in a:
    if i%2 !=0: 
        b.append(i)
print(b)

