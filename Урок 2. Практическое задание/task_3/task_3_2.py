"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def mirror_number(user_input, new_number=0):
    if user_input == 0:
        return print(f'Число наооборот {new_number}')
    new_number = new_number * 10 + user_input % 10
    user_input //= 10
    return mirror_number(user_input, new_number)


mirror_number(int(input('Введите натуральное число: ')))
