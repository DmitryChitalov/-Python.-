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
    user_number = int(input('Введите целое число: '))
    res = ''
    while user_number != 0:
        res += str(user_number % 10)
        user_number //= 10
    print(f'Перевернутое число: {res}')
except ValueError:
    print('Необходимо ввести целое число')