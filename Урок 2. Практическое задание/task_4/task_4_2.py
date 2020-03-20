"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion_sum(num_el, element=1, total=0, count=0):
    """
    Сумма n элементов через рекурсию
    """
    # Переменная для вывода кол-ва элементов
    count += 1
    # Сумма элементов
    total += element
    element /= -2
    num_el -= 1
    if num_el == 0:
        return print(f"Количество элементов - {count}, их сумма - {total}")
    return recursion_sum(num_el, element, total, count)


try:
    NUM_EL = int(input("Введите количество элементов: "))
    recursion_sum(NUM_EL)
except ValueError:
    print("Введите корректное значение")
