def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

n = int(input('Данные 1: '))
m = int(input('Данные 2: '))
number = factorial(n) / (factorial(m) * factorial(n-m))
print(number)









