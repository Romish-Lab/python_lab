# 15. Given a year, determine whether it is a leap year. If it is a leap year, return True otherwise return False.
# In the Gregorian calendar, leap year conditions:
# - Year divisible by 4 is leap year, unless divisible by 100 and not divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True (Leap Year)")
else:
    print("False (Not a Leap Year)")