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
NUMBER = int(input('Введите трехзначное число: '))
AMOUNT = NUMBER // 100 + ((NUMBER // 10) % 10) + NUMBER % 10
MULTIPLY = (NUMBER // 100) * ((NUMBER // 10) % 10) * (NUMBER % 10)
print(AMOUNT)
print(MULTIPLY)
