# 16. Write a Python program to sort a list alphabetically in a dictionary.
num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for k in num_dict:
    num_dict[k].sort()
print(num_dict)
