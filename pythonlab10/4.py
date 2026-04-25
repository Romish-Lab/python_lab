# 4. Append text to poem.txt and show the file.

def append_poem(text):
    with open("poem.txt", "a") as f:
        f.write("\n" + text)
append_poem("This is an added line.")

