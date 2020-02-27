def func_fib(x):
    if x == 1 or x == 2:
        return 1
    return func_fib(x - 1) + func_fib(x - 2)

n = int(input('Число: '))
fib = func_fib(n)
print(fib)