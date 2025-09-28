x = "hello"
print(x[::-1])
x1 = [11,12,11,23,23,4,5,3,2,23,2,3,2,2,3]
uniq = []
dupl = []
for i in x1:
    if i in uniq:
        dupl.append(i)
    else:
        uniq.append(i)
x2 = set(dupl)
print(list(x2))

x3 = "ababA"
if x3.strip().lower() == x3[::-1].strip().lower():
    print("Yes")
else:
    print("No")
x = list(range(1,11))
y = list(range(21,31))
print(x)
print(y)
print(sorted(y+x))

def fizzBuzz(num):
    for i1 in range(1, num):
        if i1 % 3 == 0 and i1 % 5 == 0:
            print("FizzBuzz", i1)
        elif i1 % 3 == 0:
            print("Fizz", i1)
        elif i1 % 5 == 0:
            print("Buzz", i1)
        else:
            pass
fizzBuzz(16)

y = [x for x in range(1, 20) if x % 3 != 0]
print(y)

g = [x for x in range(100) if x % 10 == 0]
print(g)

h1 ={x:x*x for x in range(1,101) if x % 10 == 0}
print(h1)
print(type(h1))

with open("data.txt","rt") as f:
    #data1 = f.read()
    data2 = f.readline()
    #data3 = f.readlines()
    #print(data1)
    #print(type(data1))
    print(data2)
    print(type(data2))
    print(data2.count("l"))
    #print(data3)
    #print(type(data3))
