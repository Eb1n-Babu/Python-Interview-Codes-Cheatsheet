def fibonacci(n):
    fib = [0, 1]
    for i in range(n):
        fib.append(fib[-1] + fib[-2])
    print(fib)


fibonacci(10)