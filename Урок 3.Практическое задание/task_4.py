"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

user_array = [random.randint(-100, 100) for i in range(30)]
numb = max(user_array, key=user_array.count)
print(f'в нашем списке "{user_array}" \nчисло {numb} встречается {user_array.count(numb)} раз(a), это чаще всего!')
