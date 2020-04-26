"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""

try:
    NUM = int(input('Введите трехзначное число:'))

    HUN = NUM // 100
    DECI = (NUM // 10) % 10
    UNI = NUM % 10

    print(f"Сотая часть числа = {HUN} "
          "Десятичная часть числа = {DECI} "
          "Единичная часть числа {UNI}")
    print(f"Сумма цифр = {HUN + DECI + UNI}")
    print(f"Произведение цифр = {HUN * DECI * UNI}")
except ValueError:
    print(f"Нужно ввести число. Попробуйте снова.")
