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

userInt = int(input('Введите трехзначное число: '))
firstUserInt = userInt // 100
secondUserInt = (userInt // 10) % 10
thirdUserInt = userInt % 10
sumUserInt = firstUserInt + secondUserInt + thirdUserInt
mulUserInt = firstUserInt * secondUserInt * thirdUserInt
print(
    f'Сумма цифр введенного числа: {firstUserInt} + {secondUserInt} + {thirdUserInt} = {sumUserInt}')
print(
    f'Произведение цифр введенного числа: {firstUserInt} * {secondUserInt} * {thirdUserInt} = {mulUserInt}')
