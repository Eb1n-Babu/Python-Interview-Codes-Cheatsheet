class Test:
    x = 20
    def __init__(self , a, b):
        self.a = a  # instance member argument
        self.b = b  # instance member argument

    def show(self):
        print(self.a , self.b)

print(Test.x) # class object
t1 = Test(4,8)  # instance object
t1.show()