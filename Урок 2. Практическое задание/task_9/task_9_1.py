"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ но я решил сделать только рекурсию
ибо с циклами и так давно все понятно
"""

# ТУТ БУДЕТ РЕШЕНИЕ - РЕШЕТО ЭРАТОСФЕНА

SERIES_OF_NUMBERS = []
FIRST_EL = 2
LAST_EL = 34
for el in range(LAST_EL - 1):
    SERIES_OF_NUMBERS.append(el + FIRST_EL)

print(SERIES_OF_NUMBERS)

for el in SERIES_OF_NUMBERS:
    if el * el < LAST_EL:
        for further_el in SERIES_OF_NUMBERS[el:]:
            if further_el % el == 0:
                SERIES_OF_NUMBERS.remove(further_el)
    else:
        break

print(SERIES_OF_NUMBERS)
