# 21. Write a Python program to find the specified number of maximum values in a dictionary.
d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max_val = max(d.values())
print([k for k, v in d.items() if v == max_val])    
print(sorted(d.values(), reverse=True)[:2])         
print(sorted(d.values(), reverse=True)[:5])         

