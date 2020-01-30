def fibo(x):
    fb1 = 1
    fb2 = 1
    s = 1
    for i in range(3, x + 1):
        s = fb1 + fb2
        fb1 = fb2
        fb2 = s
    return s

n = int(input('Число: '))
number = fibo(n)
print(number)
