"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
qwe = [1, 2, 3, 2, 3, 4, 2, 3, 4, 6, 5, 4, 5, 5, 5, 5, 5, 5, 6]
asd = max(qwe, key=lambda x: qwe.count(x))
print(f'число {asd} в массиве встречается чаще всего')

# 2 вариант

elem = qwe[2]
count = 0
for i in range(len(qwe)):
    ccc = 0
    for j in range(i + 1, len(qwe)):
        if qwe[i] == qwe[j]:
            ccc += 1
    if count < ccc:
        count = ccc
        elem = qwe[i]
print(f'число {elem} в  массиве встречается чаще всего {count} раз')
