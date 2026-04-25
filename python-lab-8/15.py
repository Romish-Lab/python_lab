# 15. Write a Python function that takes two words and checks if both start with the same letter.

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
if word1[0].lower() == word2[0].lower():
    print("Both words start with the same letter.")
else:
    print("The words start with different letters.")