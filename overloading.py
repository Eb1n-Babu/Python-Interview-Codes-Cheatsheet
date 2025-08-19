def l1(*args):
    print(args)

l1(1, 2, 3)

def l2(**kwargs):
    print(kwargs)

l2(name="bob",age=20)


def l4(name, age =40):
    print(name, age)
    print(name,60)

l4(name="bob",age=20)

def add(*t):
    print(sum(t))

add(1,2,3,4,5)
