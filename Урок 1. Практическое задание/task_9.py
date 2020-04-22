"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
NUM_ONE = int(input('Введите первое число: '))
NUM_TWO = int(input('Введите второе число: '))
NUM_THREE = int(input('Введите третье число: '))
if NUM_THREE > NUM_ONE > NUM_TWO or NUM_THREE < NUM_ONE < NUM_TWO:
    print(f"среднее число: {NUM_ONE}")
elif NUM_ONE > NUM_TWO > NUM_THREE or NUM_ONE < NUM_TWO < NUM_THREE:
    print(f"среднее число: {NUM_TWO}")
elif NUM_ONE > NUM_THREE > NUM_TWO or NUM_ONE < NUM_THREE < NUM_TWO:
    print(f"среднее число: {NUM_THREE}")
elif NUM_ONE == NUM_TWO == NUM_THREE:
    print('Все числа равны.')
else:
    print('Два числа из трех равны, среднего нет.')
