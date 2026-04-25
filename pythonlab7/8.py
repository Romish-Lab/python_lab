# 8. Write a Python function to find the maximum and minimum value, 
# sum and multiplication of all the numbers in a list.
def list_info(lst):
    mx = max(lst)
    mn = min(lst)
    sm = sum(lst)
    prod = 1
    for x in lst:
        prod *= x
    return mx, mn, sm, prod

print(list_info([4, 20, 5, 0]))
