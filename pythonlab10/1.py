# 1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.
def write_poem():
    poem = """Roses are red,
Violets are blue,
Python feels easy,
When learning with you."""
    with open("poem.txt", "w") as f:
        f.write(poem)

def read_poem():
    with open("poem.txt", "r") as f:
        print(f.read())

write_poem()
read_poem()


