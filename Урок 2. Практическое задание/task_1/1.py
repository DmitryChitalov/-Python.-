while True:
    MATH_OPERATION = input('Калькулятор\nВведите операцию (+, -, , / или 0 для выхода): ')

    if MATH_OPERATION == '0':
        print('Вы вышли из программы.')
        break
    if MATH_OPERATION in {'+', '-', '/', ''}:
        NUM_1 = int(input('Введите первое число: '))
        NUM_2 = int(input('Введите второе число: '))
        if MATH_OPERATION == '+':
            answer = NUM_1 + NUM_2
            print(f'Сумма чисел {NUM_1} и {NUM_2} = {answer}')
        elif MATH_OPERATION == '-':
            answer = NUM_1 - NUM_2
            print(f'Разность чисел {NUM_1} и {NUM_2} = {answer}')
        elif MATH_OPERATION == '*':
            answer = NUM_1 * NUM_2
            print(f'Произведение чисел {NUM_1} и {NUM_2} = {answer}')
        elif MATH_OPERATION == '/':
            if NUM_2 != 0:
                answer = NUM_1 / NUM_2
                print(f'Деление чисел {NUM_1} и {NUM_2} = {answer}')
            else:
                print('Делить на 0 нельзя!')
    else:
        print('Вы ввели не корректную операцию.')