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
from collections import deque

def add(hex_num, hex_num_2):
    ''' сумма 16-ричных чисел'''
    tmp_1 = hex_num.copy()
    tmp_2 = hex_num_2.copy()
    res_hex = deque()
    rest = 0

    while len(tmp_1) or len(tmp_2) or rest:
        tmp = rest
        if len(tmp_1):
            tmp += int(tmp_1.pop(), 16)
        if len(tmp_2):
            tmp += int(tmp_2.pop(), 16)
        rest = tmp // 16
        tmp %= 16
        res_hex.appendleft(f'{tmp:X}')
    return res_hex


# Произведение двух 16-ричных чисел
def multiply(hex_num, hex_num_2):
    ''' мумножение 16-ричных чисел'''
    tmp_1 = hex_num.copy()
    res_hex = deque()
    rest = 0
    # Представляем очередь как 16-ричное число
    tmp_num = int(''.join([i for i in hex_num_2]), 16)
    # Умножаем пока не опустеют очереди или пока есть перенос разрядов
    while len(tmp_1) or rest:
        tmp = rest
        if len(tmp_1):
            tmp = tmp + int(tmp_1.pop(), 16) * tmp_num
        rest = tmp // 16
        tmp %= 16
        res_hex.appendleft(f'{tmp:X}')
    return res_hex


NUMBER_1 = input('Введите шестнадцатеричное число\n')
HEX_NUM = deque(NUMBER_1)
NUMBER_2 = input('Введите второе шестнадцатеричное число\n')
HEX_NUM_2 = deque(NUMBER_2)

SUMM = add(HEX_NUM, HEX_NUM_2)
MULTYPLY = multiply(HEX_NUM, HEX_NUM_2)
print(SUMM)
print(MULTYPLY)