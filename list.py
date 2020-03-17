# x = int(input('Длина массива: '))
# a = []
# while len(a) < x:
#     number = int(input('Число: '))
#     a.append(number)
# print(a)


x = int(input('Длина массива: '))
n = int(input('Число: '))
a = []
a.append(n)
for i,elem in enumerate(a):
    print(i, elem)