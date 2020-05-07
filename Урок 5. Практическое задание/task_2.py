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
import collections

NUMBERS = collections.defaultdict(list)

def decision():

    for i in range(2):
        j = input(f'Введите {i + 1}-е шестнадцатиричное число: ')
        NUMBERS[i] = list(j)
    number_1 = ''.join(NUMBERS[0])
    number_2 = ''.join(NUMBERS[1])
    decimal_numb = [int(''.join(n), 16) for n in NUMBERS.values()]
    hex_numb = hex(sum(decimal_numb)).upper()
    print(f"{number_1.upper()} + {number_2.upper()} = {hex_numb[2:]}")

    decimal_numb = [int(''.join(n), 16) for n in NUMBERS.values()]
    hex_numb = hex(decimal_numb[0] * decimal_numb[1]).upper()
    print(f"{number_1.upper()} * {number_2.upper()} = {hex_numb[2:]}")

decision()
