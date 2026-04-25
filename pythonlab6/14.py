# 14. Write a Python program to sort a dictionary by its values.
d = {'b': 2, 'a': 1, 'c': 3}
print(dict(sorted(d.items(), key=lambda x: x[1])))
