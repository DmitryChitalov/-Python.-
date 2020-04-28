"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""


def find_mults(array, number):
    """ Finds how many items in array are multiples of number"""
    result = []
    for k in array:
        if k % number == 0:
            result.append(i)
    return f' {number}: {len(result)}'


EXAMPLE = [a for a in range(2, 100)]

for i in range(2, 10):
    print(find_mults(EXAMPLE, i))

print('*' * 20)

ANOTHER_ARRAY = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            ANOTHER_ARRAY[j - 2] += 1

for i, item in enumerate(ANOTHER_ARRAY, start=2):
    print(f' {i}: {item}')
