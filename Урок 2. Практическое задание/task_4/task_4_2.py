"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def recursion(number, result, item):
    """Рекурсия решения фцнкции"""
    if number == 0:
        print(result)
        return
    result = result + item
    item = item / (- 2)
    number = number - 1
    recursion(number, result, item)

# start
recursion(int(input(f"Введите число: ")), 0, 1)
