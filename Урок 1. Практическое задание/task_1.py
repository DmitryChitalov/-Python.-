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

users_input = int(input("Enter you number which contains 3 digits: "))

first = users_input // 100
second = (users_input // 10) % 10
third = users_input % 10


# print(first)
# print(second)
# print(third)

print(f"The sum of digits from your number is {first + second + third}")
print(f"The multiplication of digits from your number is {first * second * third}")
