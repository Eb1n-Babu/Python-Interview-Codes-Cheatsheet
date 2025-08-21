import math


def alphabet(n):
    for i in range(0, n ):
        print((i+1)*(chr(65+i)))
alphabet(10)
print("====================")

def alphabet1(n):
    for i in range(n, -1 ,-1):
        print((i+1)*(chr(65+i)))
alphabet1(10)

print("=============")

def num(n):
    for i in range(0,n,+2):
        print((' '*(n-i)),(i+1)*(chr(65+i)))
num(10)