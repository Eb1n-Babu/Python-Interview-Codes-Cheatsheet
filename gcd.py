import math


def gcd(a,b):
    if a==0 or a==b:
        return b
    if b==0:
        return a
    if a>b:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                return i
            else:
                continue
    elif b>a:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                return i
            else:
                continue
    return None


print(gcd(2,3))
print(gcd(2,4))

def fun_gcd(a,b):
    return math.gcd(a,b)

print(fun_gcd(2,3))
print(fun_gcd(2,4))
