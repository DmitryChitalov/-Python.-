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


# 1st version
try:
    number = int(input("Enter three-digit positive number:"))
    if 100 > number or number > 999:
        raise TypeError("Error! You should enter three-digit positive number")
    hundreds = number // 100
    tens = (number % 100) // 10
    units = number % 10
    splitted_num_sum = hundreds + tens + units
    print(f"Sum of {number} elements = {splitted_num_sum}")
except TypeError as te:
    print(te)
except ValueError:
    print("Only numbers should be entered.")
except Exception as ex:
    print(ex)


# 2nd version
try:
    number = int(input("Enter three-digit positive number:"))
    if 100 > number or number > 999:
        raise TypeError("Error! You should enter three-digit positive number")
    splitted_num_sum = sum(map(int, str(number)))
    print(f"Sum of {number} elements = {splitted_num_sum}")
except TypeError as te:
    print(te)
except ValueError:
    print("Only numbers should be entered.")
except Exception as ex:
    print(ex)

