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

number = int(input("Введите натуральное число: "))
num = number
i = len(str(number))
odd_digits = 0
even_digits = 0
while i > 0:
    if ((number % 10) % 2) == 0:
        even_digits += 1
        number = number // 10
    else:
        odd_digits += 1
        number = number // 10
    i -= 1

print("В числе", str(num), "всего", str(len(str(num))), "цифр, из которых",
      str(even_digits), "чётных и", str(odd_digits), "нечётных")
