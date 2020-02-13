def func_number(x):
    unit = 0
    while x > 0:
        n = x % 10
        x = x // 10
        if n == 1:
            unit += 1
    return unit

number = int(input('Число: '))
print(func_number(number))





