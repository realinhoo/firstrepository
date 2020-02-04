def clock(x):
    for i in range(n, 0, -2):
        for j in range((n-i) // 2):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()
    for i in range(3, n + 1, 2):
        for j in range((n-i) // 2):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()




n = int(input('Данные 1: '))
print(clock(n))