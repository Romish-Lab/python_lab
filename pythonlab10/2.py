# 2. Read first n lines from poem.txt.

def read_first_n(n):
    with open("poem.txt", "r") as f:
        for i in range(n):
            print(f.readline(), end="")

read_first_n(2)   
