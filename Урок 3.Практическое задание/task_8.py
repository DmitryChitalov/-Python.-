"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""

N = 4
M = 5

EXT_LST = []
for i in range(N):
    b = []
    print(f'{i+1}-я строка:')
    for j in range(M):
        b.append(int(input()))
    b.append(sum(b))

    EXT_LST.append(b)
print(EXT_LST[1])
for i in range(N):
    print(f"{EXT_LST[i]}\n", end='')

