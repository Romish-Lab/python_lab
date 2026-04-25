# 7. Read poem.txt line by line into an array.

def file_to_array():
    arr = []
    with open("poem.txt", "r") as f:
        for line in f:
            arr.append(line.strip())
    print(arr)
file_to_array()
