# 12. Read a random line from poem.txt.

import random

def random_line():
    with open("poem.txt", "r") as f:
        lines = f.readlines()
    print("Random line:", random.choice(lines))
random_line()
