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

numbers_1 = int(input('Укажите целое, многозначное число'))
numbers_2 = 0
print (f'Вы ввели число: {numbers_1}')

while numbers_1 > 0:
    number = numbers_1 % 10
    numbers_1 = numbers_1 // 10
    numbers_2 = numbers_2 * 10
    numbers_2 = numbers_2 + number
print(f'Обратное число введенному: {numbers_2}')