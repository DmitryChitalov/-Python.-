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

number = int(input('Введите трехзначное число: '))

digit_1 = number % 10
digit_2 = number % 100 // 10
digit_3 = number // 100

print('Сумма всех цифр введенного числа', digit_1 + digit_2 + digit_3)
print('Произведение всех цифр введенного числа', digit_1 * digit_2 * digit_3)