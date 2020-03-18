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

def year1(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(f"Год {year} - високосный")
    else:
        print(f"Год {year} - невисокосный")

try:
    YEAR = int(input("Введите год: "))
    year1(YEAR)

except ValueError:
    print("Вы ввели некоректное число")

