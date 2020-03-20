"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных
"""

while True:
    try:
        NUMBER = int(input())

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
