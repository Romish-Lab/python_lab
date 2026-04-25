# 9. Count occurrences of "the" in poem.txt.

def count_the():
    with open("poem.txt", "r") as f:
        text = f.read().lower()
    print("Occurrences of 'the':", text.count("the"))
count_the()
