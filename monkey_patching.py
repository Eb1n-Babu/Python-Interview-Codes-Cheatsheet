class Test:
    def __init__(self, x):
        self.x = x

    def get_data(self):
        print("get data")

    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()

t1 = Test(4)
print("before monkey patching")
t1.f1()
t1.f2()

def get_new_data(self):
    print("get new data")

Test.get_data = get_new_data
print("after monkey patching")
t1.f1()
t1.f2()