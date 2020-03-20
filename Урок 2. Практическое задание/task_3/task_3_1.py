"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321
"""
while True:
    try:
        NUMBER = int(input('Введите любое число: '))
        if type(NUMBER):
            break
    except ValueError:
        print('Ошибка! Введено некорректное значение!')
LEN_NUM = len(str(NUMBER))
RES = ''
UNITS = NUMBER % 10
PART_OF_NUMBER = NUMBER // 10
while LEN_NUM > 0:
    RES = RES + str(UNITS)
    UNITS = PART_OF_NUMBER % 10
    PART_OF_NUMBER = PART_OF_NUMBER // 10
    LEN_NUM -= 1
print(f'Перевернутое число: {RES}')
