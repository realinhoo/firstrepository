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



# def rev(x):
#     if x == 0:
#         return
#     one = (x + 1) % 10
#     rev(x // 10)
#     print(one, end="")

# user = int(input('Данные: '))
# rev(user)


# def sum(x):
#     if x == 0:
#         return 0
#     return (x % 10) + sum(x // 10)

# number = int(input('Число: '))
# print(sum(number))



def sumNumber(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return sumNumber(x - 1)
    else:
        return x + sumNumber(x - 2)



number = int(input('Число: '))
print(sumNumber(number))


#print(input('Число: ')[:: -1])



