def money(x):
    hundred = x // 100

    # b = x //10 % 10
    # fifty = b // 5
    
    # ten = b % 5
    # r = x % 10

    # five = r // 5
    # one = r % 5

    b = x % 100
    fifty = b // 50

    b = b % 50
    ten = b // 10

    b = b % 10
    five = b // 5
    one = b % 5

    print('100 руб: ', hundred)
    print('50 руб: ', fifty)
    print('10 руб: ', ten)
    print('5 руб: ', five)
    print('1 руб: ', one)
    

number = int(input('Число: '))
money(number)