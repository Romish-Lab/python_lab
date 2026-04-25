# Question 9: Convert a tuple of positive integers into a single integer.
a = (10, 20, 40, 5, 70)
s = ""

for x in a:
  s = s + str(x)

num = int(s)

print(num)