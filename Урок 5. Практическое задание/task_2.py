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
from collections import defaultdict
from collections import deque


def my_dex(list):
    """Преабразует строку в число"""
    dex = 0
    num = deque(list)
    num.reverse()
    for i in range(len(num)):
        dex += TABLE[num[i]] * 16 ** i
    return dex

def my_str_to_list(string):
    """Преобразуем ввод пользователя в лист"""
    result = list()
    for cnx in string:
        result.append(cnx)
    return result

def my_hex(numb):
    """Преабразует число в 16ый формат"""
    num = deque()
    while numb > 0:
        dec = numb % 16
        for i in TABLE:
            if TABLE[i] == dec:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


SIGNS = '0123456789ABCDEF'
TABLE = defaultdict(int)
COUNTER = 0
for key in SIGNS:
    TABLE[key] += COUNTER
    COUNTER += 1

NUM_1 = my_dex(my_str_to_list(input('Введите первое число в 16ом формате:\n ').upper()))
NUM_2 = my_dex(my_str_to_list(input('Введите второе число в 16ом формате:\n ').upper()))

print(f'Сумма чисел: {my_hex(NUM_1 + NUM_2)}')
print(f'Произведение чисел: {my_hex(NUM_1 * NUM_2)}')
