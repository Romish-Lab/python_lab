# 19. Write a Python program to insert a given string at the beginning of all items in a list.
a = [1, 2, 3, 4]
b = 'emp'
a = [b + str(c) for c in a]
print(a)
