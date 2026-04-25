# 3. Count lines in poem.txt starting with 'T'.

def count_T():
    c = 0
    with open("poem.txt", "r") as f:
        for line in f:
            if line.startswith("T"):
                c += 1
    print("Lines starting with T:", c)

count_T()
