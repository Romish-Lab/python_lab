# Question 11: Compute the sum of all the elements of each tuple stored inside a list of tuples.
#first
a = [(1, 2), (2, 3), (3, 4)]
b = [sum(x) for x in a]
print("First :")
print(b)
#second
c = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
d = [sum(y) for y in c]

print("Second")
print(d)