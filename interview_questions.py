x = "hello"
print(x[::-1])

x1 = "malayalamfg"

if x1.strip().lower() == x1[::-1].strip().lower():
    print("palindrome")
else:
    print("not palindrome")

def fib_seq(n):
    fib = [0, 1]
    for i in range(0,n-2):
        fib.append(fib[-1] + fib[-2])
    print(fib)

fib_seq(10)

def fact_(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
fact_(4)

m1 = [1, 2, 3, 2, 4, 3]

def duplicat(m1):
    unique = []
    duplicate = []
    for element in m1:
        if element in unique:
            duplicate.append(element)
        else:
            unique.append(element)
    x5 = set(duplicate)
    print(list(x5))


duplicat(m1)

x = list(range(1,11))
y = list(range(11,21))

def dict_cre(x,y):
    if len(x) == len(y):
        return dict(zip(x,y))
    else:
        return f"x and y must have same length"

print(dict_cre(x,y))

x7 = list(range(1,11))
print(x7)

