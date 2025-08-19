class Test:
    def __init__(self):
        self.a = 5

    def f1(self):
        self.b = 7

t1 = Test()
t2 = Test()
print(t1.a)
t1.c = 5
t1.d = 7
print(t1.c)

print(t1.__dict__)
