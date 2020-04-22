"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.
"""

# Решение через  "ветвление"
while True:
    try:
        YEAR = int(input('Введите год : '))
        if (YEAR % 4 == 0 and YEAR % 100 != 0) or YEAR % 400 == 0:
            print(f'Год {YEAR} високосный')
        else:
            print(f'Год {YEAR} обычный')
        break
    except ValueError or TypeError:
        print('Ошибка ввода. Значением года является число.')
# Решение через тернарный оператор
while True:
    try:
        YEAR = int(input('Введите год : '))
        print(f'Год {YEAR} високосный') if (YEAR % 4 == 0 and YEAR % 100 != 0) or YEAR % 400 == 0 else \
            print(f'Год {YEAR} обычный')
        break
    except ValueError or TypeError:
        print('Ошибка ввода. Значением года является число.')
