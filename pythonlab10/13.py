# 13. Remove newline characters from poem.txt.

def remove_newlines():
    lst = []
    with open("poem.txt", "r") as f:
        for line in f:
            lst.append(line.strip())
    print(lst)
remove_newlines()
