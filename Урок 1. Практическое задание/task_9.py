"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

a = 1
b = 2
c = 3

"1 - вариант "
if a == b and b == c:
    print(f'Все числа равны\n')
elif a == b or a == c or b == c:
    if a == b:
        print(f' Числo c  являются средними\n')
    elif a == c:
        print(f' Числo b являются средними\n')
    else:
        print(f' Число a является средним\n')

elif b < a < c or c < a < b:
    print(f' Число a является средним\n')

elif a < b < c or c < b < a:
        print(f' Число b является средним\n')

else:
    print(f' Число с является средним\n')

"2 - вариант "
if a == b == c:
    print(f'Все числа равны\n')
elif b <= a <= c or c <= a < b:
    if a == b:
        print(f' Число с является средним\n')
    elif a == c:
        print(f' Число b является средним\n')
    else:
        print(f' Число a является средним\n')
elif a < b <= c or c <= b < a:
    if b == c:
        print(f' Число a является средним\n')
    else:
        print(f' Число b является средним\n')

else:
    print(f' Число с является средним\n')
