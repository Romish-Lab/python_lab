# 11. Copy poem.txt to new_poem.txt.

def copy_poem():
    with open("poem.txt", "r") as a, open("new_poem.txt", "w") as b:
        b.write(a.read())
    print("poem.txt copied to new_poem.txt")
copy_poem()
