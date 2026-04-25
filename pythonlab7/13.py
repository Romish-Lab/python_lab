# 13. Write a Python function that checks whether a passed string is a palindrome or not.
def check(s):
    return s == s[::-1]

print(check("madam"))   
print(check("python"))  
