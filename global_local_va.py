x = 5
def global_local_var():
    global x
    x = 15
    y = 20
    a = x+y
    print(a)
    print("inside function :", x)

global_local_var()
print("out side function :", x)