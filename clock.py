def clock(x, s):
    for i in range(n, 0, -2):
        for j in range((n-i) // 2 + s):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()

    for i in range(3, n + 1, 2):
        for j in range((n-i) // 2 + s):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()

n = int(input('Данные: '))
s = int(input('Отступ: '))

print(clock(n, s))




















