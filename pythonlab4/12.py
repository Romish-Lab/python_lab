# 12. Write a Python Program to merge two lists and removes all duplicates from the combined list.
a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
d = []
for e in c:
    if e not in d:
        d.append(e)
print(d)
