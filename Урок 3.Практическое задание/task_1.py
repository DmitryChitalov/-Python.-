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

counts = [0] * 8
for i in range(2, 100):
    if (i % 2) == 0:
        counts[0] += 1
    if (i % 3) == 0:
        counts[1] += 1
    if (i % 4) == 0:
        counts[2] += 1
    if (i % 5) == 0:
        counts[3] += 1
    if (i % 6) == 0:
        counts[4] += 1
    if (i % 7) == 0:
        counts[5] += 1
    if (i % 8) == 0:
        counts[6] += 1
    if (i % 9) == 0:
        counts[7] += 1

for i in range(8):
    print(f"В диапазоне 2-99: {counts[i]} чисел кратны {i + 2}")
