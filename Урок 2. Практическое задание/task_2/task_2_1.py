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

ENTER_NUM = int(input('Введите число: '))
EVEN = 0
ODD = 0

print(f'В числе {ENTER_NUM}')

while ENTER_NUM != 0:
    NUM = ENTER_NUM % 10
    if NUM % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    ENTER_NUM = ENTER_NUM // 10

# Подсчет общего количества цифр, сначала хотел сделать счетчиком в цикле,
# но тогда пришлось бы писать на одну строку больше (объявление и счетчик),
# а результат тот-же
COUNT = EVEN + ODD

print(f'Всего: {COUNT} цифр, из них:')
print(f'{EVEN} - четных')
print(f'{ODD} - нечетных')
