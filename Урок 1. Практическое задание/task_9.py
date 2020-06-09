"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
a = int(input('Enter 1  number : '))
b = int(input('Enter 2  number : '))
c = int(input('Enter 3  number : '))

if a == b == c:
    print('числа равны')
elif a < b < c or c < b < a:
    print(f'число {b} среднее')
elif b < a < c or c < a < b:
    print(f'число {a} среднее')
elif a < c < b or b < c < a:
    print(f'число {c} среднее')
