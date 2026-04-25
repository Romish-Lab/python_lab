# 6. Write a Python program to guess a number between 1 and 9. Keep asking until the guess is correct. Use random.
import random
a = random.randint(1, 9)
while True:
    b = int(input("Guess the number (1-9): "))
    if b == a:
        print("Well guessed!")
        break
