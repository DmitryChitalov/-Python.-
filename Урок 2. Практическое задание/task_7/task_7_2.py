"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def sum_seq(num):
	if num == 1:
		return num
	else:
		return num + sum_seq(num - 1)

try:
	NUM = int(input('Введите целое число: '))
	SUM_A = sum_seq(NUM)
	print(SUM_A)
	SUM_B = int(NUM * (NUM + 1) / 2)
	print(SUM_B)
	
	print(SUM_A == SUM_B)
	
except ValueError:
	print('Ошибка, нужно ввести целое число!')
	






	

