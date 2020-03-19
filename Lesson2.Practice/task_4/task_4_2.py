"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def get_sum(count_el, first_el, current_count, sum):
    if current_count == count_el:
        return sum
    else:
        sum += first_el
        return get_sum(count_el, first_el / -2, current_count + 1, sum)


if __name__ == "__main__":
    SUM = 0
    CURR_COUNT = 0
    try:
        COUNT_EL = int(input("Введите количество элементов: "))
        if COUNT_EL < 0:
            print("Количество элементов должно быть неотрицательным")
        else:
            print(get_sum(COUNT_EL, 1, CURR_COUNT, SUM))
    except ValueError:
        print("Ошибка ввода значений")