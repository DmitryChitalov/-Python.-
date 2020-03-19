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


try:
    NUM = int(input("Введите натуральное число: "))
except BaseException:
    print("Неверно введено число")

count_even = 0
count_odd = 0
flag = True
while flag:
    digit = NUM % 10
    if digit % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
    NUM = NUM // 10
    if NUM == 0:
        flag = False

print(f"Четные {count_even}")
print(f"Нечетные {count_odd}")
print(f"Всего цифр {count_even + count_odd}")

