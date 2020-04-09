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


from collections import deque, namedtuple


def oop_solution(value_1, value_2) -> None:
    """ ООП + стандартные преобразования, без коллекций """
    class HexValue:
        """ Класс hex чисел """
        def __init__(self, val):
            self.val = int(''.join(val), 16)

        def __add__(self, other):
            return hex(self.val + other.val)[2:]

        def __mul__(self, other):
            return hex(self.val * other.val)[2:]

    val_1 = HexValue(value_1)
    val_2 = HexValue(value_2)
    print(f'ООП результат сложения: {(val_1 + val_2).upper()}')
    print(f'ООП результат умножения: {(val_1 * val_2).upper()}')


def collections_solution(data) -> None:
    """ Стандартные преобразования + работа с коллекциями """

    def to_string(item):
        result = ''
        for _ in range(len(item)):
            result += item.popleft()
        return result

    val_1 = data.val_1
    val_2 = data.val_2
    val_1 = to_string(val_1)
    val_2 = to_string(val_2)

    result_sum = hex(int(val_1, 16) + int(val_2, 16))[2:]
    result_mult = hex(int(val_1, 16) * int(val_2, 16))[2:]
    print(f'Коллекции результат сложения: {result_sum.upper()}')
    print(f'Коллекции результат умножения: {result_mult.upper()}')


if __name__ == "__main__":
    VAL_1 = (input('Ведите первое шестнадцатеричное число: ').strip())
    VAL_2 = (input('Ведите второе шестнадцатеричное число: ').strip())
    VAL_1 = deque(VAL_1)
    VAL_2 = deque(VAL_2)
    oop_solution(VAL_1, VAL_2)

    # Упаковка в коллекцию
    InputedDdata = namedtuple('InData', ['val_1', 'val_2'])
    INPUTED_DATA = InputedDdata(val_1=VAL_1, val_2=VAL_2)

    collections_solution(INPUTED_DATA)
