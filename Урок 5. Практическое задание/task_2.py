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

# Коллекция для сохранения введеных пользователем чисел
NUMBERS_COLLECTION = deque()
# Коллекция для сохранения суммы введеных пользователем чисел
SUM_NUMBERS = deque()
# Коллекция для сохранения произведения введеных пользователем чисел
MUL_NUMBERS = deque()

while True:
    # Запрос пользователя на ввод чисел в шестнадцатиричном формате
    NUMBERS = input('Введите 2 шестнадцатиричных числа через пробел:\n').split()
    try:
        # Проверка, что введено 2 числа
        if len(NUMBERS) != 2:
            raise IOError
        else:
            # Попытка перевода в шестнадцатиричный формат введенных чисел
            [hex(int(float.fromhex(elem))) for elem in NUMBERS]
    except (ValueError, TypeError, IOError):
        print(f'Ошибка ввода чисел.\n'
              f'Необходимо ввести 2 числа в шестнадцатиричном формате через пробел.')
    else:
        j = 0
        # Сохранение чисел посимвольно в коллекцию
        for elements in NUMBERS:
            NUMBERS_COLLECTION.append([])
            for i in elements:
                NUMBERS_COLLECTION[j].append(i)
            j += 1

        # Инициализация значений суммы и произведения чисел
        SUM = '0.0'
        MUL_NUM = '0.0'
        MUL = '0.0'

        # Цикл восстановления первого числа в коллекции из цифр числа.
        for i, element in enumerate(NUMBERS_COLLECTION[0]):
            SUM = hex(int(float.fromhex(element)*pow(16, len(NUMBERS_COLLECTION[0]) - 1 - i) + float.fromhex(SUM)))
        # Цикл восстановления второго числа в коллекции из цифр числа.
        for i, element in enumerate(NUMBERS_COLLECTION[1]):
            SUM = hex(int(float.fromhex(element)*pow(16, len(NUMBERS_COLLECTION[1]) - 1 - i) + float.fromhex(SUM)))
        # Цикл нахождения произведения двух чисел
        for i, element in enumerate(NUMBERS_COLLECTION[0]):
            for j, value in enumerate(NUMBERS_COLLECTION[1]):
                MUL_NUM = hex(int(float.fromhex(element)*pow(16, len(NUMBERS_COLLECTION[0]) - 1 - i) *
                              float.fromhex(value)*pow(16, len(NUMBERS_COLLECTION[1]) - 1 - j)))
                MUL = hex(int(float.fromhex(MUL_NUM) + float.fromhex(MUL)))
        # Добавление результатов суммы и произведения в соответствующие коллекции
        for element in SUM[2:]:
            SUM_NUMBERS.append(element)
        for element in MUL[2:]:
            MUL_NUMBERS.append(element)
        print(f'Сумма чисел: {SUM_NUMBERS}')
        print(f'Произведение чисел: {MUL_NUMBERS}')
        break
