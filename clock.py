def clock(x, s):
    for i in range(x, 0, -2):
        for j in range(((x-i) // 2) + s):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print('')
    for i in range(3, x + 1, 2):
        for j in range(((x-i) // 2) + s):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print('')

n = int(input('Данные: '))
s = int(input('Отступ: '))

for i in range(n, 0, -2):
    s += 1
    clock(i,s)
for i in range(3, n + 1, 2):
    s -= 1
    clock(i,s)

















