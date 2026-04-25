# 3. Write a Python function to calculate the factorial of a number 
def fact_iter(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n-1)

print(fact_rec(0))