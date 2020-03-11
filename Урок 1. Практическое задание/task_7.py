"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
EDGE_A = None
EDGE_B = None
EDGE_C = None

while not isinstance(EDGE_A, float) or not isinstance(EDGE_B, float) or not isinstance(EDGE_C, float):
	EDGE_A = input('Введите длину стороны А: ')
	EDGE_B = input('Введите длину стороны В: ')
	EDGE_C = input('Введите длину стороны С: ')
	try:
		EDGE_A = float(EDGE_A)
		EDGE_B = float(EDGE_B)
		EDGE_C = float(EDGE_C)
	except ValueError:
		print('Ошибка, нужно вводить число!')

if EDGE_A + EDGE_B > EDGE_C and EDGE_A + EDGE_C > EDGE_B and EDGE_C + EDGE_B > EDGE_A:
	print('Треугольник существует')
	if EDGE_A == EDGE_B == EDGE_C:
		print('Треугольник равносторонний')
	elif EDGE_A == EDGE_B != EDGE_C or EDGE_A != EDGE_B == EDGE_C or EDGE_C == EDGE_A != EDGE_A:
		print('Треугольник равнобедренный')
	else:
		print('Треугольник разносторонний')
else:
	print('Такой треугольник не существует!')