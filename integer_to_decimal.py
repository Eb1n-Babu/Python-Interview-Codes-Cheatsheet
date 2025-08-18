import decimal

def integer_to_decimal(n):
    print("================================================")
    n = int(n)
    print(n , type(n))
    print(n ,type(decimal.Decimal(n)))
    print("===============================================")

if __name__ == '__main__':
    try:
        integer_to_decimal(5)
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")