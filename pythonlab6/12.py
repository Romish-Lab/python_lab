# 12. Write a Python program to find all keys in a dictionary that have the given value.
d = {'a': 1, 'b': 2, 'c': 1}
val = 1
for k, v in d.items():
    if v == val:
        print(k)
