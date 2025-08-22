import math

print("===============================================================================================================")
def star(n):
    for i in range(1,n+1):
        print(i*"* ")
star(5)
print("================================================================================================================")
def number_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(j,end=" ")
        print()
number_pyramid(10)
print("================================================================================================================")
def number_order_pyramid(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num+=1
        print()
number_order_pyramid(5)
print("================================================================================================================")
def alphabet_pyramid(n):
    for i in range(0,n+1):
        print(chr(65+i)*(i+1))
alphabet_pyramid(5)
print("================================================================================================================")
def alphabet_pyramid_reverse(n):
    for i in range(n,-1,-1):
        print(chr(65+i)*(i+1))
alphabet_pyramid_reverse(5)
print("================================================================================================================")
def odd_alphabet_pyramid(n):
    for i in range(0,n+1,+2):
        print(chr(65+i)*(i+1))

odd_alphabet_pyramid(5)
print("================================================================================================================")
def alphabet_odd_pyramid_v1(n):
    p=65
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        for j in range(i+1):
            print(chr(p),end=" ")
        for j in range(i):
            print(chr(p),end=" ")
        p+=1
        print()
alphabet_odd_pyramid_v1(5)
print("================================================================================================================")
def alphabet_odd_pyramid_v2(n):
    for i in range(0,n+1):
        print(' '*(n-i),end=" ")
        for j in  range(0,i+1):
            print(chr(65+i),end=" ")
        print()
alphabet_odd_pyramid_v2(5)
print("================================================================================================================")
def order_pyramid_v2(n):
    num = 1
    for i in range(0,n+1):
        for j in range(0,i+1):
            print(num,end=" ")
            num+=1
        print()
order_pyramid_v2(5)
print("================================================================================================================")
def alphabet_order_pyramid(n):
    p = 65
    for i in range(0,n+1):
        for j in range(0,i+1):
            print(chr(p),end=" ")
            p+=1
        print()
alphabet_order_pyramid(5)
print("================================================================================================================")
def alphabet_order_pyramid_reverse(n):
    p = 65
    for i in range(0,n+1):
        for j in range(n,i,-1):
            print(chr(p),end=" ")
            p+=1
        print()
alphabet_order_pyramid_reverse(5)
print("================================================================================================================")
def alphabet_order_pyramid_v3(n):
   p = 65
   for i in range(n):
       for j in range(0,i+1):
           print(" ",end=" ")
       for j in range(i,n):
           print(chr(p),end=" ")
           p+=1
       print()
alphabet_order_pyramid_v3(5)
print("=================================================================================================================")
def alphabet_order_pyramid_v4(n):
    p = 65
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(0,i+1):
            print(chr(p),end=" ")
            p+=1
        print()
alphabet_order_pyramid_v4(5)
print("=================================================================================================================")
def alphabet_odd_pyramid_v2(n):
    for i in range(0,n):
        print(' '*(n-i),end=" ")
        for j in  range(0,i+1):
            print(chr(65+j),end=" ")
        print()
alphabet_odd_pyramid_v2(5)
print("=================================================================================================================")
def alphabet_odd_pyramid_v3(n):
    p = 65
    for i in range(0,n):
        print(' '*(n-i),end=" ")
        for j in range(0,i+1):
            print(chr(p+i),end=" ")
        print()
alphabet_odd_pyramid_v3(5)
print("=================================================================================================================")
def alphabet_odd_pyramid_v4(n):
    p = 65
    for i in range(n):
        print(' '*(n-i),end=" ")
        for j in range(0,i+1):
            print(chr(p),end=" ")
            p+=1
        print()
alphabet_odd_pyramid_v4(5)
print("=================================================================================================================")
def pyramid_with_start(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*" , end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
pyramid_with_start(5)
print("=================================================================================================================")
def pyramid_with_start_v1(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*  " , end=" ")
        print()
pyramid_with_start_v1(5)
print("=================================================================================================================")
def sandGlass(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
sandGlass(5)
print("=================================================================================================================")
def sandGlass_v1(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(0,n-i):
            print("*",end=" ")
        for j in range(1,n-i):
            print("*",end=" ")
        print()
    for k in range(n):
        for j in range(0,n-k-1):
            print(" ",end=" ")
        for j in range(0,k+1):
            print("*",end=" ")
        for j in range(k):
            print("*",end=" ")
        print()

sandGlass_v1(5)

print("=================================================================================================================")
def butterfly(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for m in range(n-k-1):
            print("*",end=" ")
        print()
butterfly(8)
print("=================================================================================================================")
def butterfly_v1(n):
    for i in range(0,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for j in range(0,k+1):
            print(" ",end=" ")
        for j in range(0,n-k):
            print("*",end=" ")
        print()
butterfly_v1(5)
print("=================================================================================================================")
def butterfly(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for m in range(n-k-1):
            print("*",end=" ")
        print()
butterfly(5)
def butterfly_v2(n):
    for i in range(0,n+1):
        for j in range(n-i+n):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for j in range(0,k+1+n):
            print(" ",end=" ")
        for j in range(0,n-k):
            print("*",end=" ")
        print()
butterfly_v2(5)
print("=================================================================================================================")
def butterfly_v2(n):
    for i in range(0,n+1):
        for j in range(n-i+n):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for j in range(0,k+1+n):
            print(" ",end=" ")
        for j in range(0,n-k):
            print("*",end=" ")
        print()
butterfly_v2(5)
print("=================================================================================================================")
def butterfly_v6(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for m in range(n-k-1):
            print("*",end=" ")
        print()
    for i in range(0,n+1):
        for j in range(n-i+n):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()
    for k in range(n):
        for j in range(0,k+1+n):
            print(" ",end=" ")
        for j in range(0,n-k):
            print("*",end=" ")
        print()
butterfly_v6(5)
print("==================================================================================================")
def number_order_pyramid(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        print()
number_order_pyramid(10)
print("==================================================================================================")
def fun_(n):
    for i in range(0,n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(n,i,-1):
            print(j,end=" ")
        print()
fun_(5)
print("==================================================================================================")
def square(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
square(10)
print("==================================================================================================")
def plus(n):
    for i in range(n):
        for j in range(n):
            if j==math.ceil(n/2) or i==math.floor(n/2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
plus(10)