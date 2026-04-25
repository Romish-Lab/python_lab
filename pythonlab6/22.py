# 22. Write a Python program to find the key of maximum and minimum values in a dictionary.
d = {'a': 5, 'b': 14, 'c': 32, 'd': 35}
max_key = max(d, key=d.get)
min_key = min(d, key=d.get)
print(max_key, min_key)
