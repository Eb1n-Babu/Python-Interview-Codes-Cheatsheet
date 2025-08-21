class A:
    def __init__(self):
        self.a = 10

class B:
    def __init__(self):
        self.b = 20
class C(A):
    def __init__(self , a):
        super().__init__()
        self.a = a
        self.c = 30


C1 = C(50)
print(C1.c)
print(C1.a)