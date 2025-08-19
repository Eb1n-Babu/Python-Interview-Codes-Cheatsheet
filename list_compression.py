def list_c(n):
    l1 = [2*i for i in range(1,10)]
    return l1

print(list_c(5))

list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

l2 = [e for e in list1 if e%2==0]
print(l2)

l3 = [i*2 for i in range(1,10)]
print(l3)