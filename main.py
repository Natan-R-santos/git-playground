def adicao():
    a = float(input('Insert a number: '))
    b = float(input('Insert a number: '))
    c= float(input('Insert a number: '))
    result = a + b + c
    print(f'The result is: {result}')

while True:
    a = int(input('Insert a number: '))
    if a ==1:
        print('hello world')
        adicao()
    elif a ==2:
        print('hello world')
    elif a ==3:
        print('hello world')
    elif a ==4:
        print('hello world')
    elif a ==5:
        print('hello world')
    elif a ==0:
        print('Exit system')
        break
    else:
        print('Invalid number!')