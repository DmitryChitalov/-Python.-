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

# вариант 1

try:
    NUMBER = int(input("Введите число: "))
    INVERTED_NUMBER = ''
    while NUMBER > 0:
        N = NUMBER % 10
        NUMBER = NUMBER // 10
        INVERTED_NUMBER += str(N)
    print(f"Перевернутое число: {int(INVERTED_NUMBER)}")
except ValueError:
    print("Неправильный ввод данных.")

# вариант 2

try:
    NUMBER = int(input("Введите число: "))
    INVERTED_NUMBER = 0
    while NUMBER > 0:
        INVERTED_NUMBER = INVERTED_NUMBER * 10 + NUMBER % 10
        NUMBER = NUMBER // 10
    print(f"Перевернутое число: {INVERTED_NUMBER}.")
except ValueError:
    print("Неправильный ввод данных.")
