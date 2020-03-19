"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

try:
    NUM = abs(int(input('Введите число: ')))  # Вдруг палец попадет на минус...
    print('Перевернутое число: ', end='')
    if NUM != 0:
        while NUM:
            print(NUM % 10, end='')
            NUM //= 10
    else:
        print('0')
except ValueError as err:
    print(f'Ошибка ввода: {err}')

# Еще вариант через собирание строки
# print('\n')  # перенос строки на случай совместного запуска 2 вариантов
# try:
#     NUM = abs(int(input('Введите число: ')))
#     VICE_VERSA = 0 if NUM == 0 else ''
#     while NUM:
#         VICE_VERSA += str(NUM % 10)
#         NUM //= 10
#     print(f'Перевернутое число: {VICE_VERSA}')
# except ValueError as err:
#     print(f'Неверное ввод, ошибка: {err}')
