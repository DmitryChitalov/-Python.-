"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
SUM_A = 0
SUM_B = 0
ITEM = 1

try:
	NUM = int(input('Введите целое число: '))
	SUM_B = int(NUM * (NUM + 1) / 2)
	print(SUM_B)
	while NUM > 0:
		SUM_A = SUM_A + ITEM
		ITEM = ITEM + 1
		NUM = NUM - 1
	print(SUM_A)
	print(SUM_A == SUM_B)
except ValueError:
	print('Ошибка, нужно ввести целое число!')
