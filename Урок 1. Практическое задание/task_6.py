"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""
MIN = 1
MAX = 26
NUM_A = None


while not isinstance(NUM_A, int):
	NUM_A = input(f"Введите целое число от {MIN} до {MAX}: ")
	try:
		NUM_A = int(NUM_A)
	except ValueError:
		print('Ошибка, нужно вводить целое число! \n')

try:
	if not MIN <= NUM_A <= MAX:
		raise ValueError(f"Число лежит вне интервала [{MIN}; {MAX}]!")
	LETTER = chr(ord('a') + NUM_A - 1)
	print(LETTER)
except ValueError as err:
	print("Будьте внимательны:", err)
