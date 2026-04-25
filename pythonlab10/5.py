# 5. Read poem.txt into a list.

def file_to_list():
    lst = []
    with open("poem.txt", "r") as f:
        for line in f:
            lst.append(line.strip())
    print(lst)
file_to_list()
