def lucky(x):
    b1 = 0
    for i in range(3):
        b1 = b1 + x % 10
        x = x // 10

    b2 = 0
    for i in range(3):
        b2 = b2 + x % 10
        x = x // 10
    
    return b1 == b2
    
ticket_number_start = int(input('Введите номер: '))
ticket_number_end = int(input('Введите номер: '))

if lucky(ticket_number):
    print("Счастливый")
else:
    print("Не счастливый")

q = 0
for i in range(ticket_number_start, ticket_number_end):
    q += 1
print(q)












#n = 0
#s = int(input('Ввести данные: '))
#while s > 0:
#    n = n + s % 10
#    s = s // 10
#print(n)







