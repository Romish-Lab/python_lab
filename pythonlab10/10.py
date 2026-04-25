# 10. Write list items into poem.txt.

def write_list_to_poem(items):
    with open("poem.txt", "w") as f:
        for x in items:
            f.write(x + "\n")

write_list_to_poem(["Apple", "Ball", "Cat"])

