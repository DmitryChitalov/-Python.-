"""
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


result = []
for i in range(2, 10):
    result.append(0)
    for j in range(2, 100):
        if j % i == 0:
            result[i - 2] += 1

for i in range(2, 10):
    print(f"В диапазоне 2-99: {result[i - 2]} чисел кратны {i}")
