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

a = input('Введите  число')
b = (len(a))
c = 0
d = 0
while b != 0:
    c += (int(a) % (10 ** b) // (10 ** (b - 1))) * (10 ** d)
    d += 1
    b -= 1

print(f'перевернутое число: {c}')