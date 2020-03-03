# def func_fib(x):
#    if x == 1 or x == 2:
#        return 1
#    return func_fib(x - 1) + func_fib(x - 2)

# n = int(input('Число: '))
# fib = func_fib(n)
# print(fib)

# def factorial(x):
#     if x == 0:
#         return 1
#     return x * factorial(x - 1)
# number = int(input('Число: '))
# print(factorial(number))



def rev(x):
    if x == 0:
        return
    rev(x // 10)
    one = x % 10
    print(one, end="")
    

user = int(input('Данные: '))
rev(user)




# n = int(input('Число '))
# one  = 0
# while n != 0:
#     one = n % 10
#     print(one, end='')
#     n = n // 10



# n1 = int(input('Число '))
# n2 = 0
# while n1 > 0:
#     digit = n1 % 10
#     n1 = n1 // 10
#     n2 = (n2 * 10) + digit
# print('Обратное число', n2)



#print(input('Число ')[:: -1])

