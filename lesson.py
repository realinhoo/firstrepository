#for i in range(n, 0, -2):
#    for j in range( (n - i) // 2):
#        print(' ', end='')
#    for j in range(i):
#        print('*', end='')
#    print()

#for i in range(3, n + 1, 2):
#    for j in range( (n - i) // 2):
#        print(' ', end='')
#    for j in range(i):
#        print('*', end='')
#    print()

#s = int(input('Ввести данные: '))
#for i in range(s, 0, -1):
#    for j in range(i):
#        print('*', end='')
#    print()
#for i in range(2, s + 1, 1):
#    for j in range(i):
#        print('*', end='')
#    print()

#n = int(input('Данные: '))

#for i in range(n):
#    for j in range(n):
#        if i >= j and (n - 1) <= (i + j) or i <= j and (n - 1) >= (i + j):
#            print('*', end='')
#        else:
#            print('.', end='')
#    print()
# (n - 1) <= (i + j)
# i <= j
# i <= j and (n - 1) <= (i + j)
# i >= j and (n - 1) <= (i + j)
# i <= j and (n - 1) >= (i + j)
#i >= j and (n - 1) >= (i + j) or i <= j and (n - 1) <= (i + j)




#Задачи с while

#userNumber = int(input('Данные: '))
#indexNumber = 1
#while userNumber != 0:
#    indexNumber *= userNumber
#    userNumber = int(input('Данные: '))
#print(indexNumber)

#n = 0
#while n < 100:
#    s = int(input('Введите данные: '))
#    n += s
#print(n)

#n = 0
#s = int(input('Ввести данные: '))
#while s > 0:
#    n = n + s % 10
#    s = s // 10
#print(n)



#import random
#x = random.randint(1, 100)
#s = 0
#n = 0

#while s != x:
#    s = int(input('Введите число: '))
#    n = n + 1
#    if s == x:
#        print('Угадано!')
#    elif s < x:
#        print('Загаданное число больше.')
#    else:
#        print('Загаданное число меньше.')
#print(f'Количество попыток {n}')




#number = int(input('Число: '))
#f = 1

#for i in range(1, number + 1):
#    f *= i
#print(f'Факториал равен {f}')




#x = random.randint(1, 100)
#run = True
#n = 0

#while run:
#    s = int(input('Введите число: '))
#    n = n + 1
#
#    if s == x:
#        print('Угадано!')
#        run = False
#    elif s < x:
#        print('Загаданное число больше.')
#    else:
#        print('Загаданное число меньше.')
#print(f'Количество попыток {n}')


#number = int(input('Число: '))
#f = 1

#for i in range(1, number + 1):
#    f *= i
#print(f'Факториал равен {f}')



#fb1 = 1
#fb2 = 1
#s = 1
#n = int(input('Число: '))
#for i in range(3, n + 1):
#    s = fb1 + fb2
#    fb1 = fb2
#    fb2 = s
#print(s)

n = int(input('Данные 1: '))
m = int(input('Данные 2: '))
while n < m:
    print('Не корректно')
    n = int(input('Данные 1: '))
    m = int(input('Данные 2: '))

f = 1
for i in range(1, n + 1):
    f *= i
print(f)

j = 1
for i in range(1, m + 1):
    j *= i
print(j)

k = n - m
h = 1
for i in range(1, k + 1):
    h *= i
print(h)

factorial = f // (j * h)
print(factorial)


def factorial(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

n = int(input('Данные: '))
j = factorial(n)
print(j)







