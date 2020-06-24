"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


# Solution 1
# num = input('enter a number:')
# even = 0
# odd = 0
# list_digits = list(map(int, str(num)))
# print(list_digits)
#
# for i in list_digits:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"There are {even} even digits and {odd} odd digits")


# Solution 2
# num = int(input('enter a number:'))
# even = 0
# odd = 0
# while num > 0:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     num = num // 10
# print(f"There are {even} even digits and {odd} odd digits")

#  Solution from teacher


def cycle_method(numb):
    evens = 0
    odds = 0
    while numb != 0:
        cur_n = numb % 10
        numb = numb // 10
        if cur_n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds


try:
    NUMB = int(input("Enter natural number: "))
    print(f"Number odd and eve digits in this natural number is: {cycle_method(NUMB)}")
except ValueError:
    print("You entered a wrong value. Try again")
