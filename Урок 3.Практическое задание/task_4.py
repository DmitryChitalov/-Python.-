"""
Задание_4. Определить, какое число в массиве встречается чаще всего
Подсказка: можно применить ф-цию max с параметром key
"""
import random

ARRAY_NUMBERS = [random.randint(0, 9) for _ in range(20)]
print(f'Массив случайных целых чисел: {ARRAY_NUMBERS}')
# Находим максимальное количество повторений элемента в массиве
MAX_COUNT = max(map(lambda x: ARRAY_NUMBERS.count(x), ARRAY_NUMBERS))
# Вывод списка с повторяющимися элементами
print(f'Наиболее часто повторяющиеся элементы: '
      f'{str(set(el for el in ARRAY_NUMBERS if ARRAY_NUMBERS.count(el) == MAX_COUNT))[1:-1]}')
print(f'Количество повторений: {MAX_COUNT}')
