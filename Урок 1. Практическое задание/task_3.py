"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

X1 = float(input('Enter the x coordinate of the first point: '))
Y1 = float(input('Enter the y coordinate of the first point: '))
X2 = float(input('Enter the x coordinate of the second point: '))
Y2 = float(input('Enter the y coordinate of the second point: '))

if X1 == X2 and Y1 == Y2:
    print(f'It is a point, infinitely many lines can be drawn')
elif X1 == X2:
    print(f'x = {X1}')
elif Y1 == Y2:
    print(f'y = {Y1}')
else:
    k = (Y2 - Y1) / (X2 - X1)
    B = Y2 - k * X2
    if B == 0:
        print(f'y = {k:.1f}x')
    else:
        print(f'y = {k:.1f}x + {B:.1f}')
