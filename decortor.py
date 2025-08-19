def decorator_function(func):
    def funct2():
        print("inside decorator")
        func()
        print("outside decorator")
    return funct2

@ decorator_function
def hello():
    print("hello")

hello()