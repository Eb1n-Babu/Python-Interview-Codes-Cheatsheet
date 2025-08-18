def add_two_list(lis1,list2):
    return lis1 + list2

def add(list1,list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    return list3




list1 = [1, 2, 3, 4]
list2 = [13, 14, 15, 16]


print(add_two_list(list1,list2))
print(add(list1,list2))

