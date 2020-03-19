"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""
ER_STRING = 'Ошибка ввода!'
NUM_A = 1
NUM_Z = 26
START_NUM = 96
try:
    number = int(input('введите номер буквы: '))
    if number > NUM_Z or number < NUM_A:
        print(ER_STRING)
    else:
        print('Введёному номеру соответствует буква: %s' %(chr(START_NUM + number)))
except:
    print(ER_STRING)
