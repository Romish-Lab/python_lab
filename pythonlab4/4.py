a = int(input("Enter the number of items: "))
lst = [None] * a

for b in range(a):
    lst[b] = input("Enter item: ")

lst.sort()
l = lst[-1]
s = lst[0]
print("Largest is ",l)
print("Smallest is ",s)
