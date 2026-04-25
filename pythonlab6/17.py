# 17. Given a dictionary, write a Python script to reverse key-value pairs.
d = {'a': 1, 'b': 2, 'c': 3}
rev = {v: k for k, v in d.items()}
print(rev)
