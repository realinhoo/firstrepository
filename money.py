def money(x):
    a = x // 100
    b = x % 100 // 50
    c = b % 10
    print('100 руб: ', a)
    print('50 руб: ', b)
    print('10 руб: ', c)
    
 #   print('5 руб: ', )
#    print('1 руб: ', )
    
    

number = int(input('Число: '))
money(number)