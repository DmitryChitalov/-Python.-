"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


NUM_A = None
NUM_B = None
NUM_C = None

while not isinstance(NUM_A, float) or not isinstance(NUM_B, float) or not isinstance(NUM_C, float):
	NUM_A = input('Введите число А: ')
	NUM_B = input('Введите число В: ')
	NUM_C = input('Введите число С: ')
	try:
		NUM_A = float(NUM_A)
		NUM_B = float(NUM_B)
		NUM_C = float(NUM_C)
	except ValueError:
		print('Ошибка, нужно вводить число!')

try:
	if NUM_A == NUM_B or NUM_A == NUM_C or NUM_B == NUM_C:
		raise ValueError(f"Как минимум два числа одинаковые!")
	if NUM_B < NUM_A < NUM_C:
		print(NUM_A)
	elif NUM_A < NUM_B < NUM_C:
		print(NUM_B)
	else:
		print(NUM_C)
except ValueError as err:
	print("Будьте внимательны:", err)
