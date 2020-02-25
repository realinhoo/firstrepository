import math
def prime_number(x):
    for i in range(2, int(math.sqrt(x + 1))):
        if x % i == 0:
            return False
    return True

number = int(input('Данные: '))

if prime_number(number):
    print("Простое")
else:
    print("Составное")

