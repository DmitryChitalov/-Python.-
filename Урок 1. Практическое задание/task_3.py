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

try:
    x1 = int(input("Enter x1. It should be a number:"))
    y1 = int(input("Enter y1. It should be a number:"))
    x2 = int(input("Enter x2. It should be a number:"))
    y2 = int(input("Enter y2. It should be a number:"))

    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - y2 * x1) / (x2 - x1)

    if k < 0:
        k = f"({str(k)})"
    if b < 0:
        b = f"({str(b)})"

    print(f"Equation of a Straight Line: y={k}x+{b}")

except ValueError:
    print("Only numbers should be entered.")
except Exception as ex:
    print(ex)


