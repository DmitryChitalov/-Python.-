"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
# Вот хоть убей не понял как через ПОДСКАЗКУ сделать - как смог....
l = [10, 10, 10, 10, 10, 10, 10, 12, 12, 1, 1, 3, 3, 3, 3, 3, 4, 5, 12, 3, 6, 6, 3]
a = {v: l.count(v) for v in set(l)}
print(
    f'Чаше всего в массиве встречается\n[(число, кол-во раз)]'
    f'\n{[(key, cnt) for key, cnt in a.items() if cnt == max(a.values())]}')
