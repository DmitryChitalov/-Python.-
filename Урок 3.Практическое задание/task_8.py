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

M = []
for s in range(5):
    A = []
    S = 0
    for n in range(4):
        el = int(input(f'Введите число строка {s + 1}, елемент {n + 1}: '))
        A.append(el)
        S += el
    A.append(S)
    M.append(A)
for i in range(5):
    print(M[i])
print(f'матрица {M}')
