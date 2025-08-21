import math

def prime(x):
    if x  >= 2:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    return False

if __name__ == '__main__':
    x = int(input(" Enter a number "))
    try:
        if prime(x):
            print("prime number")
        else:
            print("not prime")
    except ValueError:
        print("Not a prime number")
    except ZeroDivisionError:
        print("Not a prime number")
    except ArithmeticError:
        print("Not a prime number")

