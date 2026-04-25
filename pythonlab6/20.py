# 19. Write a Python program to find the highest 3 values in a dictionary.
d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
print(sorted(d.values(), reverse=True)[:3])
