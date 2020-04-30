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
import random
N = 5
EXT_LST = []
for i in range(N):
    z = []
    for j in range(N):
        n = int(random.randint(1, 10))
        z.append(n)
    EXT_LST.append(z)

def last_el(m):
    for k in range(0, N):
        el_last = 0
        for d in range(0, N - 1):
            el_last += m[k][d]
        m[k][N - 1] = el_last
    return m

def printMatrix(mat):
   for l in range(len(mat)):
      for o in range(len(mat[l])):
          print("{:4d}".format(mat[l][o]), end="")
      print()

printMatrix(last_el(EXT_LST))