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
sumnum1 = 0
sumnum2 = 0
sumnum3 = 0
sumnum4 = 0
sumnum5 = 0
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
a1 = input("введите числа 1 строки через пробел ").split()
a2 = input("введите числа 2 строки через пробел ").split()
a3 = input("введите числа 3 строки через пробел ").split()
a4 = input("введите числа 4 строки через пробел ").split()
a5 = input("введите числа 5 строки через пробел ").split()

for i in a1:
    sumnum1 += int(i)
    b1.append(int(i))
b1.append(sumnum1)

for e in a2:
    sumnum2 += int(e)
    b2.append(int(e))
b2.append(sumnum2)

for k in a3:
    sumnum3 += int(k)
    b3.append(int(k))
b3.append(sumnum3)

for o in a4:
    sumnum4 += int(o)
    b4.append(int(o))
b4.append(sumnum4)

for u in a5:
    sumnum5 += int(u)
    b5.append(int(u))
b5.append(sumnum5)

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)