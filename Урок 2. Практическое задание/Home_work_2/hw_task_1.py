oper = '1'
first_num = 0
sekond_num = 0

while oper != '0':
    oper = input('Введите операцию: ')
    if oper == '0':
        break
    elif oper == '+':
        first_num = int(input('1-е число: '))
        sekond_num = int(input('2-е число: '))
        print(f'Результат: {first_num} + {sekond_num} = {first_num + sekond_num}')
    elif oper == '-':
        first_num = int(input('1-е число: '))
        sekond_num = int(input('2-е число: '))
        print(f'Результат: {first_num} - {sekond_num} = {first_num - sekond_num}')
    elif oper == '*':
        first_num = int(input('1-е число: '))
        sekond_num = int(input('2-е число: '))
        print(f'Результат: {first_num} * {sekond_num} = {first_num * sekond_num}')
    elif oper == '/':
        first_num = int(input('1-е число: '))
        sekond_num = int(input('2-е число: '))
        while sekond_num == 0:
            sekond_num = int(input('На 0 делить нельзя, введите другое число: '))
        print(f'Результат: {first_num} / {sekond_num} = {first_num / sekond_num}')
    else:
        print('Вы ввели неправильное число...')
