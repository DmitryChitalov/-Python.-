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


def converse(NUM):
    NUMBER = deque()
    while NUM > 0:
        SYMBOL = NUM % 16
        for i in HEX_DICT:
            if HEX_DICT[i] == SYMBOL:
                NUMBER.append(i)
        NUM //= 16
    NUMBER.reverse()
    return NUMBER

HEX_SYM = '0123456789ABCDEF'
HEX_DICT = defaultdict(int)
count = 0
for k in HEX_SYM:
    HEX_DICT[k] += count
    count += 1

NUM_1 = int((input('Введите первое число в шестнадцатиричном формате: ')), 16)
NUM_2 = int((input('Введите первое число в шестнадцатиричном формате: ')), 16)

print(converse(NUM_1+NUM_2))
print(converse(NUM_1 * NUM_2))
