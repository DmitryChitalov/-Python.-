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

class HexNumber:
    """Перегрузка методов"""
    def __init__(self, hex_num):
        self.number = list(hex_num)

    def __str__(self):
        return self.number.__str__()

    def __add__(self, other):
        # сообщаем, что число находится в 16-ой системе счисления и возвращаем
        # его значение в 10-ой системе счисления
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 + numb_2)[2:].upper()}')

    def __mul__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 * numb_2)[2:].upper()}')


# numb_a = input(f'Введите 1-е шестнадцатиричное число: ').upper()
# numb_b = input(f'Введите 2-е шестнадцатиричное число: ').upper()
# hex_numb_1 = HexNumber(numb_a)
# hex_numb_2 = HexNumber(numb_b)
# print(f'{list(numb_a)} + {list(numb_b)} = {hex_numb_1 + hex_numb_2}')
# print(f'{list(numb_a)} * {list(numb_b)} = {hex_numb_1 * hex_numb_2}')

print(int("11",2))
print(int("2",8))
print(int("2",10))
print(int("2",16))