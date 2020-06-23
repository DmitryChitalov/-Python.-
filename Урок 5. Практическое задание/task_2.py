"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict, OrderedDict

user_number = defaultdict(list)
for i in range(2):
    user_num = input('Введите шестнадцетеричное число: ')
    user_number[i] = list(user_num)
summ = sum([int(''.join(j), 16) for j in user_number.values()])
print(f'Сумма введеных чисел: {list(hex(summ))[2:]}')
multiplication = int(''.join(user_number[0]), 16) * int(''.join(user_number[1]), 16)
print(f'Произведение введеных чисел: {list(hex(multiplication))[2:]}')
# Второй вариант, правда он почти не отличается от первого
user_number = OrderedDict()
for i in range(2):
    user_num = input('Введите шестнадцетеричное число: ')
    user_number[i] = list(user_num)
summ = sum([int(''.join(j), 16) for j in user_number.values()])
print(f'Сумма введеных чисел: {list(hex(summ))[2:]}')
multiplication = int(''.join(user_number[0]), 16) * int(''.join(user_number[1]), 16)
print(f'Произведение введеных чисел: {list(hex(multiplication))[2:]}')
