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

x1 = float(input('Enter the x coordinate of the first point: '))
y1 = float(input('Enter the y coordinate of the first point: '))
x2 = float(input('Enter the x coordinate of the second point: '))
y2 = float(input('Enter the y coordinate of the second point: '))

if x1 == x2 and y1 == y2:
    print(f'It is a point, infinitely many lines can be drawn')
elif x1 == x2:
    print(f'x = {x1}')
elif y1 == y2:
    print(f'y = {y1}')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y2 - k * x2
    if b == 0:
        print(f'y = {k:.1f}x')
    else:
        print(f'y = {k:.1f}x + {b:.1f}')
