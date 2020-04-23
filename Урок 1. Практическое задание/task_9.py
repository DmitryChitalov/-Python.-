"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).
Подсказка: можно добавить проверку, что введены равные числа
"""
num_a = int(input('Первое число: '))
num_b = int(input('Второе число: '))
num_c = int(input('Третье число: '))

if num_a == num_b or num_a == num_c or num_b == num_c:
    print('Введены равные числа!')
elif num_a > num_b > num_c or num_a < num_b < num_c:
    print(f'Среднее число: {num_b}')
elif num_c > num_a > num_b or num_c < num_a < num_b:
    print(f'Среднее число: {num_a}')
else:
    print(f'Среднее число: {num_c}')
