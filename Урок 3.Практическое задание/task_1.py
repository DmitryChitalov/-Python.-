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
LIST_OF_NUMBERS = []

for i in range(100):
    if i != 0 and i != 1:
        LIST_OF_NUMBERS.append(i)
print(LIST_OF_NUMBERS)
for i in range(10):
    COUNTER = 0
    if i != 0 and i != 1:
        for item in LIST_OF_NUMBERS:
            if item % i == 0:
                COUNTER += 1
        print(f'В диапазоне 2-99: {COUNTER} чисел кратны {i}')
