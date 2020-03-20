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


# с помощью if - else
ER_STTRING = 'ошибка ввода!'
try:
    year = int(input('введите год: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print('високосный')
    else:
        print('невисокосный')
except:
    print(ER_STTRING)



# С помощью тернарного оператора
ER_STTRING = 'ошибка ввода!'
try:
    year = int(input('введите год: '))
    print(('невисокосный', 'високосный')[year % 4 == 0 and year % 100 != 0 or year % 400 ==0])

except:
    print(ER_STTRING)