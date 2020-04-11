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


def hex_to_dec(hexademic: list):
    """Перевод числа из шестнадцатиричного в десятичное"""
    conversion_table = {'0': 0,
                        '1': 1,
                        '2': 2,
                        '3': 3,
                        '4': 4,
                        '5': 5,
                        '6': 6,
                        '7': 7,
                        '8': 8,
                        '9': 9,
                        'A': 10,
                        'B': 11,
                        'C': 12,
                        'D': 13,
                        'E': 14,
                        'F': 15
                        }
    hex_number = deque(hexademic)
    hex_number.reverse()
    dec_number = 0
    for i in range(len(hex_number)):
        dec_number += conversion_table[hex_number[i]] * 16 ** i
    return dec_number


def dec_to_hex(decim):
    """Перевод числа из десятичного в шестнадцатиричное"""
    hexademic = hex(decim)
    return hexademic


NUM_1 = list(input("Введите первое 16-тиричное число: "))
NUM_2 = list(input("Введите второе 16-тиричное число: "))
AMOUNT = hex_to_dec(NUM_1) + hex_to_dec(NUM_2)
MULTIPLICATION = hex_to_dec(NUM_1) * hex_to_dec(NUM_2)
print(f"{''.join(NUM_1)} + {''.join(NUM_2)} = {dec_to_hex(AMOUNT)[2:].upper()}")
print(f"{''.join(NUM_1)} * {''.join(NUM_2)} = {dec_to_hex(MULTIPLICATION)[2:].upper()}")
