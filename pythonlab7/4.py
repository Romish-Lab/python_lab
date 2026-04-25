# 4. Write a python function that takes two parameters length and width 
def rect(l, b):
    area = l * b
    peri = 2 * (l + b)
    return area, peri

print(rect(5, 10))
