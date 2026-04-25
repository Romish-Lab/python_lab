# 7. Write a Python program to input n numbers from user, count even and odd numbers, and stop when input is 0.

n = int(input("Enter the maximum number of times you want to loop: "))
for y in range(1, n + 1):
    b = int(input("Enter a number or enter 0 to stop: "))
    if b == 0:
        print("You entered 0 stopping the loop.")
        break 
    if(b%2==0): print("You entered even number")
    else:print("you entered odd humber")

print("Loop finished.")


