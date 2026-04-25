# 14. Extract each character of poem.txt into a list.

def extract_chars():
    with open("poem.txt", "r") as f:
        chars = list(f.read())
    print(chars)
extract_chars()
