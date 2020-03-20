"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def number_of_elements():
    number = input("Enter the number of items: ")
    if number.isdigit():
        return int(number)
    else:
        print("Invalid number. Repeat entry.")
        return number_of_elements()


def sum_of_elements(number, count=0, sum_el=0):
    if count == number:
        return sum_el
    if count % 2 == 0:
        sum_el += 1 / pow(2, count)
        count += 1
        return sum_of_elements(number, count, sum_el)
    else:
        sum_el -= 1 / pow(2, count)
        count += 1
        return sum_of_elements(number, count, sum_el)


NUMBER = number_of_elements()

print(f"Number of elements - {NUMBER}, their sum - {sum_of_elements(NUMBER)}")

