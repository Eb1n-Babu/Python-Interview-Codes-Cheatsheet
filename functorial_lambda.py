import math


def factorial(n):
    return math.factorial(n)

print(factorial(5))

def factorial1(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial1(5))


x = lambda n:1 if n == 0 else n*x(n-1)
print(x(5))

