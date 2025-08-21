def decorator_updated(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorator_updated
def hello():
    print("hello")

hello()
