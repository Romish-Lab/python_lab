# 8. Count total words in poem.txt.

def count_words():
    with open("poem.txt", "r") as f:
        text = f.read()
    print("Total words:", len(text.split()))
count_words()
