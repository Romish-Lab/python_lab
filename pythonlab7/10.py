# 10. Create a function that takes a list and a number, return a list after adding the number to the list preventing it from changing the original list.
def add_num(lst, n):
    new_lst = lst[:]
    new_lst.append(n)
    return new_lst

numbers = [1, 2, 3]
print(add_num(numbers, 4))   
