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

X1_VAL = None
Y1_VAL = None
X2_VAL = None
Y2_VAL = None

while not isinstance(X1_VAL, float) or not isinstance(Y1_VAL, float):
	X1_VAL = input('Введите значение координаты X1: \n')
	Y1_VAL = input('Введите значение координаты Y1: \n')
	try:
		X1_VAL = float(X1_VAL)
		Y1_VAL = float(Y1_VAL)
	except ValueError:
		print('Ошибка, нужно вводить число!')

while not isinstance(X2_VAL, float) or not isinstance(Y2_VAL, float):
	X2_VAL = input('Введите значение координаты X2: \n')
	Y2_VAL = input('Введите значение координаты Y2: \n')
	try:
		X2_VAL = float(X2_VAL)
		Y2_VAL = float(Y2_VAL)
	except ValueError:
		print('Ошибка, нужно вводить целое число!')

K_ANG = (Y1_VAL - Y2_VAL) / (X1_VAL - X2_VAL)
B_CONST = Y2_VAL - K_ANG * X2_VAL

print(f'Уровнение прямой: y = {K_ANG}x + {B_CONST}')
