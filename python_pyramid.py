def pyramid(n):
    for i in range(1, n):
        print(' '*(n-i),i*" *" , end="")
        print()

pyramid(10)