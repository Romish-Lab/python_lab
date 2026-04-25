# 8. Write a Python script to check whether the key 'email' exists. If not print 'key not found'.
d = {'name': 'Hari', 'age': 29, 'city': 'Bhaktapur'}
if 'email' in d:
    print(d['email'])
else:
    print("key not found")
