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


user_number = int(input("Type the number - "))

first_num = user_number // 100
second_num = (user_number // 10) % 10
third_num = user_number % 10

sum = first_num + second_num + third_num
mult = first_num * second_num * third_num

print(f"Summary - {sum}")
print(f"Multiplication - {mult}")
