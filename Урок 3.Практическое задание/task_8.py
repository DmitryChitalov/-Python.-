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

n = 5
m = 4
a = []

for i in range(n):
    str = []
    s = 0
    print(f'{i+1} строка: ')
    for j in range(m):
        q = int(input())
        s += q
        str.append(q)
    str.append(s)
    a.append(str)

for i in a:
    print(i)



q = int(input('Введите элемента массива: '))

A = [ [q for j in range(m)] for i in range(n)]
print(A)


print(A)

        # Считываем размеры массива
    s = raw_input()
    s = s.split()
    n = int(s[5])
    m = int(s[5])

    # Создаем массив
    A = range(n)
    for i in range(n):
        A[i] = range(m)

    # Считываем массив с клавиатуры
    for i in range(n):
        s = raw_input()
        s = s.split()
        for j in range(m):
            A[i][j] = int(s[j])


    # Выводим массив на экран
    for i in range(n):
        for j in range(m):
            print(A[i][j])

n = 5
m = 4
q = int(input('Введи элемент массива: '))
A = [ [q for j in range(m)] for i in range(n)]

for i in range(n):
    A.append
print(A)