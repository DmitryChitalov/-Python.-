"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

qwe = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
print(qwe)
ma = qwe[5]
mi = qwe[3]
for p in qwe:
    if p > ma:
        ma = p
    elif p < mi:
        mi = p

max_ind = qwe.index(ma)
min_ind = qwe.index(mi)

qwe[max_ind], qwe[min_ind] = qwe[min_ind], qwe[max_ind]
print(f'В данном  массиве чисел максимальное число  {ma}  стоит на '
      f'{min_ind}  позиции,'
      f' а минимальное число {mi}  стоит на  {max_ind}  позиции:  ')
print(qwe)
