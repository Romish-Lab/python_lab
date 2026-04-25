# Question 12: Demonstrate various set operations.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Set a:", a)
print("Set b:", b)
print()
# Union
c = a.union(b)
print("Union of a and b:", c)
print()
# Intersection
d = a.intersection(b)
print("Intersection of a and b:", d)
print()
# Difference
e = a.difference(b)
print("Difference (a - b):", e)
print()
# Symmetric Difference
f = a.symmetric_difference(b)
print("Symmetric Difference of a and b:", f)
print()
# Length, Max, Min of a set
print("Length of set a:", len(a))
print("Maximum value in set a:", max(a))
print("Minimum value in set a:", min(a))