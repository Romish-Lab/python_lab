# 9. Write a Python program to develop a rock paper scissors game using user input. Stop the game when user presses 'n'.
import random
a = ['rock', 'paper', 'scissors']
while True:
    b = input("Enter rock/paper/scissors or 'n' to stop: ")
    if b == 'n':
        break
    c = random.choice(a)
    print("Computer chose:", c)
    if b == c:
        print("Draw!")
    elif (b == 'rock' and c == 'scissors') or (b == 'scissors' and c == 'paper') or (b == 'paper' and c == 'rock'):
        print("You win!")
    else:
        print("You lose!")
