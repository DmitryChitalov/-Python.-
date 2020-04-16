from memory_profiler import profile

"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
"""Python 3.7.4 ОС 64bit"""

USER_NUMBER = int(input('Введите любое многозначное число: '))


@profile
def calc():
    operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operator == '0':
        print('Выход')
        return
    elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print('Некорректный ввод!')
        calc()
    operand_1 = int(input('Введите первое число: '))
    operand_2 = int(input('Введите второе число: '))
    if operator == '+':
        print(f'Ваш результат: {operand_1 + operand_2}')
    elif operator == '-':
        print(f'Ваш результат: {operand_1 - operand_2}')
    elif operator == '*':
        print(f'Ваш результат: {operand_1 * operand_2}')
    elif operator == '/':
        print(f'Ваш результат: {operand_1 / operand_2}')
    calc()


@profile
def even_odd():
    while True:
        try:
            NUMBER = int(input('Введите еще одно любое число: '))

            if type(NUMBER):
                break
        except ValueError:
            print('Введено некорректное значение! Введите число!')
    LEN_NUM = len(str(NUMBER))
    COUNT_NUM = LEN_NUM
    UNITS = NUMBER % 10
    REMAINDER_OF_NUMBER = NUMBER // 10
    EVENT_COUNT = 0
    ODD_COUNT = 0
    while LEN_NUM >= 0:
        if UNITS != 0 and UNITS % 2 == 0:
            EVENT_COUNT += 1
        elif UNITS != 0 and UNITS % 2 != 0:
            ODD_COUNT += 1
        UNITS = REMAINDER_OF_NUMBER % 10
        REMAINDER_OF_NUMBER = REMAINDER_OF_NUMBER // 10
        LEN_NUM -= 1
    print(f'В числе {NUMBER} всего {COUNT_NUM} цифр, из которых {EVENT_COUNT} чётных и {ODD_COUNT} нечётных')


def units(num):
    return num % 10


@profile
def parse_number(number, even=0, odd=0):
    unit = units(number)
    if unit % 2 == 0:
        even += 1
    elif unit % 2 != 0:
        odd += 1
    if number < 10:
        print(f'Количество четных и нечетных цифр в числе равно: {(even, odd)}')
    else:
        parse_number(number // 10, even, odd)


print('Вызов первой функции')
calc()
print('Вызов второй функции')
even_odd()
print('Вызов третьей функции')
parse_number(USER_NUMBER)

"""
Результат проверки: 


Введите любое многозначное число: 1647
Вызов первой функции
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 3
Введите второе число: 6
Ваш результат: 9
Введите операцию (+, -, *, / или 0 для выхода): 0
Выход
Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    21     13.8 MiB     13.8 MiB   @profile
    22                             def calc():
    23     13.8 MiB      0.0 MiB       operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    24     13.8 MiB      0.0 MiB       if operator == '0':
    25     13.8 MiB      0.0 MiB           print('Выход')
    26     13.8 MiB      0.0 MiB           return
    27                                 elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
    28                                     print('Некорректный ввод!')
    29                                     calc()
    30                                 operand_1 = int(input('Введите первое число: '))
    31                                 operand_2 = int(input('Введите второе число: '))
    32                                 if operator == '+':
    33                                     print(f'Ваш результат: {operand_1 + operand_2}')
    34                                 elif operator == '-':
    35                                     print(f'Ваш результат: {operand_1 - operand_2}')
    36                                 elif operator == '*':
    37                                     print(f'Ваш результат: {operand_1 * operand_2}')
    38                                 elif operator == '/':
    39                                     print(f'Ваш результат: {operand_1 / operand_2}')
    40                                 calc()


Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    21     13.8 MiB     13.8 MiB   @profile
    22                             def calc():
    23     13.8 MiB      0.0 MiB       operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    24     13.8 MiB      0.0 MiB       if operator == '0':
    25     13.8 MiB      0.0 MiB           print('Выход')
    26     13.8 MiB      0.0 MiB           return
    27     13.8 MiB      0.0 MiB       elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
    28                                     print('Некорректный ввод!')
    29                                     calc()
    30     13.8 MiB      0.0 MiB       operand_1 = int(input('Введите первое число: '))
    31     13.8 MiB      0.0 MiB       operand_2 = int(input('Введите второе число: '))
    32     13.8 MiB      0.0 MiB       if operator == '+':
    33     13.8 MiB      0.0 MiB           print(f'Ваш результат: {operand_1 + operand_2}')
    34                                 elif operator == '-':
    35                                     print(f'Ваш результат: {operand_1 - operand_2}')
    36                                 elif operator == '*':
    37                                     print(f'Ваш результат: {operand_1 * operand_2}')
    38                                 elif operator == '/':
    39                                     print(f'Ваш результат: {operand_1 / operand_2}')
    40     13.8 MiB      0.0 MiB       calc()


Вызов второй функции
Введите еще одно любое число: 87412
В числе 87412 всего 5 цифр, из которых 3 чётных и 2 нечётных
Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    43     13.8 MiB     13.8 MiB   @profile
    44                             def even_odd():
    45                                 while True:
    46     13.8 MiB      0.0 MiB           try:
    47     13.8 MiB      0.0 MiB               NUMBER = int(input('Введите еще одно любое число: '))
    48                             
    49     13.8 MiB      0.0 MiB               if type(NUMBER):
    50     13.8 MiB      0.0 MiB                   break
    51                                     except ValueError:
    52                                         print('Введено некорректное значение! Введите число!')
    53     13.8 MiB      0.0 MiB       LEN_NUM = len(str(NUMBER))
    54     13.8 MiB      0.0 MiB       COUNT_NUM = LEN_NUM
    55     13.8 MiB      0.0 MiB       UNITS = NUMBER % 10
    56     13.8 MiB      0.0 MiB       REMAINDER_OF_NUMBER = NUMBER // 10
    57     13.8 MiB      0.0 MiB       EVENT_COUNT = 0
    58     13.8 MiB      0.0 MiB       ODD_COUNT = 0
    59     13.8 MiB      0.0 MiB       while LEN_NUM >= 0:
    60     13.8 MiB      0.0 MiB           if UNITS != 0 and UNITS % 2 == 0:
    61     13.8 MiB      0.0 MiB               EVENT_COUNT += 1
    62     13.8 MiB      0.0 MiB           elif UNITS != 0 and UNITS % 2 != 0:
    63     13.8 MiB      0.0 MiB               ODD_COUNT += 1
    64     13.8 MiB      0.0 MiB           UNITS = REMAINDER_OF_NUMBER % 10
    65     13.8 MiB      0.0 MiB           REMAINDER_OF_NUMBER = REMAINDER_OF_NUMBER // 10
    66     13.8 MiB      0.0 MiB           LEN_NUM -= 1
    67     13.8 MiB      0.0 MiB       print(f'В числе {NUMBER} всего {COUNT_NUM} цифр, из которых {EVENT_COUNT} чётных и {ODD_COUNT} нечётных')


Вызов третьей функции
Количество четных и нечетных цифр в числе равно: (2, 2)
Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    74     13.8 MiB     13.8 MiB   @profile
    75                             def parse_number(number, even=0, odd=0):
    76     13.8 MiB      0.0 MiB       unit = units(number)
    77     13.8 MiB      0.0 MiB       if unit % 2 == 0:
    78                                     even += 1
    79     13.8 MiB      0.0 MiB       elif unit % 2 != 0:
    80     13.8 MiB      0.0 MiB           odd += 1
    81     13.8 MiB      0.0 MiB       if number < 10:
    82     13.8 MiB      0.0 MiB           print(f'Количество четных и нечетных цифр в числе равно: {(even, odd)}')
    83                                 else:
    84                                     parse_number(number // 10, even, odd)


Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    74     13.8 MiB     13.8 MiB   @profile
    75                             def parse_number(number, even=0, odd=0):
    76     13.8 MiB      0.0 MiB       unit = units(number)
    77     13.8 MiB      0.0 MiB       if unit % 2 == 0:
    78     13.8 MiB      0.0 MiB           even += 1
    79     13.8 MiB      0.0 MiB       elif unit % 2 != 0:
    80     13.8 MiB      0.0 MiB           odd += 1
    81     13.8 MiB      0.0 MiB       if number < 10:
    82     13.8 MiB      0.0 MiB           print(f'Количество четных и нечетных цифр в числе равно: {(even, odd)}')
    83                                 else:
    84     13.8 MiB      0.0 MiB           parse_number(number // 10, even, odd)


Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    74     13.8 MiB     13.8 MiB   @profile
    75                             def parse_number(number, even=0, odd=0):
    76     13.8 MiB      0.0 MiB       unit = units(number)
    77     13.8 MiB      0.0 MiB       if unit % 2 == 0:
    78     13.8 MiB      0.0 MiB           even += 1
    79     13.8 MiB      0.0 MiB       elif unit % 2 != 0:
    80     13.8 MiB      0.0 MiB           odd += 1
    81     13.8 MiB      0.0 MiB       if number < 10:
    82     13.8 MiB      0.0 MiB           print(f'Количество четных и нечетных цифр в числе равно: {(even, odd)}')
    83                                 else:
    84     13.8 MiB      0.0 MiB           parse_number(number // 10, even, odd)


Filename: C:/Users/IT_user/Downloads/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    74     13.8 MiB     13.8 MiB   @profile
    75                             def parse_number(number, even=0, odd=0):
    76     13.8 MiB      0.0 MiB       unit = units(number)
    77     13.8 MiB      0.0 MiB       if unit % 2 == 0:
    78     13.8 MiB      0.0 MiB           even += 1
    79     13.8 MiB      0.0 MiB       elif unit % 2 != 0:
    80     13.8 MiB      0.0 MiB           odd += 1
    81     13.8 MiB      0.0 MiB       if number < 10:
    82     13.8 MiB      0.0 MiB           print(f'Количество четных и нечетных цифр в числе равно: {(even, odd)}')
    83                                 else:
    84     13.8 MiB      0.0 MiB           parse_number(number // 10, even, odd)



Process finished with exit code 0
    
    
Здесь можно сделать вывод, что данные функции не засоряют память. Оптимизировать ничего не надо, алгоритмы написаны, 
с точки зрения потребления памяти, хорошо.    
"""
