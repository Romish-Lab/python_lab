# 11. Write a Python program to remove duplicates from a list.
a = [1, 2, 2, 3, 4, 4]
b = []
for c in a:
    if c not in b:
        b.append(c)
print(b)
