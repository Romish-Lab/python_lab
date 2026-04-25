# 18. Write a Python program to create a dictionary from a string (count frequency).
s = "engineerings"
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)
