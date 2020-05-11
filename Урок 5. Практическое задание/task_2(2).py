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

# Только ООП
class HexNumber:
    """Перегрузка методов"""
    def __init__(self, hex_num):
        self.number = list(hex_num)

    def __str__(self):
        return self.number.__str__()

    def __add__(self, other):

        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 + numb_2)[2:].upper()}')

    def __mul__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 * numb_2)[2:].upper()}')

# вводим числа
NUMB_A = input(f'Введите 1-е шестнадцатиричное число: ').upper()
NUMB_B = input(f'Введите 2-е шестнадцатиричное число: ').upper()

# считаем
HEX_NUMB_1 = HexNumber(NUMB_A)
HEX_NUMB_2 = HexNumber(NUMB_B)

# результат
print(f'{list(NUMB_A)} + {list(NUMB_B)} = {(HEX_NUMB_1 + HEX_NUMB_2)}')
print(f'{list(NUMB_A)} * {list(NUMB_B)} = {HEX_NUMB_1 * HEX_NUMB_2}')