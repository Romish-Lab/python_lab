# 14. Write a Python function that takes a string as input and counts the number  of uppercase and lowercase characters in the string.
def case(s):
    up = sum(1 for c in s if c.isupper())
    low = sum(1 for c in s if c.islower())
    return up, low
text = "Hello World!"
print(case(text))
