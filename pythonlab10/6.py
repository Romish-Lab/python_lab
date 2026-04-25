# 6. Read poem.txt into a variable.

def read_to_variable():
    with open("poem.txt", "r") as f:
        data = f.read()
    print(data)
read_to_variable()
