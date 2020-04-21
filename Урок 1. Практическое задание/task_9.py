"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

# Вариант сложный
if (b - a) * (a - c) > 0:
    print(f'The middle is {a}')
elif (a - b) * (b - c) > 0:
    print(f'The middle is {b}')
else:
    print(f'The middle is {c}')

# Вариант простой
if a > b > c or c > b > a:
    print(f'The middle is {b}')
elif b > a > c or c > a > b:
    print(f'The middle is {a}')
else:
    print(f'The middle is {c}')

if a == b or a == c or a == c:
    print('No middle')
else:
    # Любой из вариантов
    if (b - a) * (a - c) > 0:
        print(f'The middle is {a}')
    elif (a - b) * (b - c) > 0:
        print(f'The middle is {b}')
    else:
        print(f'The middle is {c}')
