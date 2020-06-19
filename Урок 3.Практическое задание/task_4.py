"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
NUMBER_LIST = [2, 8, 4, 8, 8, 9, 4, 4, 7, 2, 8, 4, 8, 2, 4, 4, 7]
TEMP_LIST = NUMBER_LIST[:]
COUNT = 0
MAX_COUNT = 0
COMMON_NUM = 0
while TEMP_LIST:
    NOW_ELEMENT = TEMP_LIST[0]
    for el in TEMP_LIST:
        if el == NOW_ELEMENT:
            COUNT += 1
    if COUNT > MAX_COUNT:
        COMMON_NUM = NOW_ELEMENT
        MAX_COUNT = COUNT
    while NOW_ELEMENT in TEMP_LIST:
        TEMP_LIST.remove(NOW_ELEMENT)
    COUNT = 0

print(f'Число {COMMON_NUM} встречается в массиве {NUMBER_LIST} чаще всего')
