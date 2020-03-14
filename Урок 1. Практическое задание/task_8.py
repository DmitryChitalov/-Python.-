"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""

# Исключим некорректный ввод с помощью обработки исключений
try:
    YEAR = int(input('Введите год: '))

# Определим является ли год високосным
    if YEAR % 4 == 0 and YEAR % 100 != 0 or YEAR % 400 == 0:
        print('Это високосный год')
    else:
        print('Этот год - не високосный')

# Тоже самое с помощью тернарного оператора
    TERNAR = 'Это високосный год' if YEAR % 4 == 0 and YEAR % 100 != 0 \
        or YEAR % 400 == 0 else 'Этот год - не високосный'
    print(TERNAR)
except ValueError:
    print('Год нужно вводить цифрой!')
