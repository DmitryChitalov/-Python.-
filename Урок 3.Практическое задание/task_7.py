"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
qwe = [28, 34, -86, -1000, 44, -37, -7, -52, -452, -19, -3, -15, -73]
print(f'Исходный массив 1: {qwe}')
mi_two = []
for i in range(2):
    mi_two.append(qwe.pop(qwe.index(min(qwe))))

aaa, zzz = mi_two

print(f'Первый Наименьший элемент: {aaa} ,'
      f' Второй наименьший элемент: {zzz} ')
print()
# 2 вариант # сортировкой
print(f'Исходный  массив 2: {qwe}')
min_fir = 0
min_sec = 1

for i in qwe:
    if qwe[min_fir] > i:
        min_sec = min_fir
        min_fir = qwe.index(i)
    elif qwe[min_sec] > i:
        min_sec = qwe.index(i)

print(f'Первый Наименьший элемент: {qwe[min_fir]} ,'
      f' Второй наименьший элемент: {qwe[min_sec]} ')
# 3 в ариант
qqq = [28, 34, -86, -1000, 44, -37, -7, -52, -452, -19, -3, -15, -73]

fel = qqq[0]
fii = 0
sel = qqq[1]
sii = 1
aaa = len(qqq)
for i in range(len(qqq)):
    if qqq[i] < fel:
        fel = qqq[i]
        fii = i
    if fel < qqq[i] < sel:
        sel = qqq[i]
        sii = i
print(fii, fel)
print(sii, sel)
