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
num_user = int(input('enter num : '))
# summ = 0
# mult = 1
# while num_user > 0:
#     remains_num_user = num_user % 10
#     summ += remains_num_user
#     mult *= remains_num_user
#     num_user //= 10
# print('сумма цифр трехзначного числа summ = %s' %summ)
# print('произведение цифр трехзначного числа mult = %s' %mult)

# summ = 0
# mult = 1
# remains_num_user = num_user % 10
# summ += remains_num_user
# mult *= remains_num_user
# num_user //= 10
#
# remains_num_user = num_user % 10
# summ += remains_num_user
# mult *= remains_num_user
# num_user //= 10
#
# remains_num_user = num_user % 10
# summ += remains_num_user
# mult *= remains_num_user
# num_user //= 10
# print('сумма цифр трехзначного числа summ = %s' % summ)
# print('произведение цифр трехзначного числа mult = %s' % mult)

first_num = num_user // 100
sec = (num_user//10) % 10
third = num_user % 10
summ = first_num+sec+third
mult = first_num*sec*third
print('сумма цифр трехзначного числа summ = %s' % summ)
print('произведение цифр трехзначного числа mult = %s' % mult)