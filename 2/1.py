print("0 завершит операцию")
while True:
    op = input("Введите оператор (*,+,-,/): ")
    if op == '0': break
    if op in ("*",'+','-','/'):
        a = float(input('a = '))
        b = float(input('b = '))
        if op == '*':
            print(f'Получилось = {a*b}')
        elif op == '+':
            print(f'Получилось = {a+b}')
        elif op == '-':
            print(f'Получилось = {a-b}')
        elif op == '/':
            if b != 0:
                print(f'Получилось = {a/b}')
            else:
                print('Деление на 0!')
    else:
        print('Невереный знак операции!')

