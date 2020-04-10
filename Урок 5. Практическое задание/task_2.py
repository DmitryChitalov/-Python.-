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
# первый вариант с использованием defaultdict

from collections import defaultdict
from functools import reduce

D = defaultdict(list)
# можно ипользовать ChainMap вместо defaultdict
# заменив на строку D = ChainMap() или обычный словарь
D['FIRST_NUM'] = [i for i in input('Введите первое число :')]
D['SECOND_NUM'] = [i for i in input('Введите второе число :')]

print(f'Первое число : {D.get("FIRST_NUM")}\n'
      f'Второе число : {D.get("SECOND_NUM")}')

# сумма чисел
AMOUNT = hex(int(reduce(lambda x, y: x+y, D.get('FIRST_NUM')), 16) +
             int(reduce(lambda x, y: x+y, D.get('SECOND_NUM')), 16))

# произведение чисел
PRODUCT = hex(int(reduce(lambda x, y: x+y, D.get('FIRST_NUM')), 16) *
              int(reduce(lambda x, y: x+y, D.get('SECOND_NUM')), 16))

print(f'Сумма чисел : {[i for i in AMOUNT.upper()[2:]]}\n'
      f'Произведение чисел : {[i for i in PRODUCT.upper()[2:]]}')


# вариант с использованием именованного кортежа

from collections import namedtuple
from functools import reduce

NUMBERS = namedtuple('NUMBERS', 'first second')
NUMBERS_TO_COUNT = NUMBERS(
      first=[i for i in input('Введите первое число :')],
      second=[i for i in input('Введите второе число :')]
)

print(f'Первое число : {NUMBERS_TO_COUNT.first}\n'
      f'Второе число : {NUMBERS_TO_COUNT.second}')

# сумма чисел
AMOUNT = hex(int(reduce(lambda x, y: x+y, NUMBERS_TO_COUNT.first), 16) +
             int(reduce(lambda x, y: x+y, NUMBERS_TO_COUNT.second), 16))

# произведение чисел
PRODUCT = hex(int(reduce(lambda x, y: x+y, NUMBERS_TO_COUNT.first), 16) *
              int(reduce(lambda x, y: x+y, NUMBERS_TO_COUNT.second), 16))

print(f'Сумма чисел : {[i for i in AMOUNT.upper()[2:]]}\n'
      f'Произведение чисел : {[i for i in PRODUCT.upper()[2:]]}')



# вариант без collection используя класс

class Numbers():
      def __init__(self, num):
            self.num = num

      def __add__(self, other):
            return Numbers(hex(int(reduce(lambda x, y: x + y, self.num), 16) +
                               int(reduce(lambda x, y: x + y, other.num), 16)))

      def __mul__(self, other):
            return Numbers(hex(int(reduce(lambda x, y: x + y, self.num), 16) *
                               int(reduce(lambda x, y: x + y, other.num), 16)))

      def __str__(self):
            return f'{[i for i in self.num[2:].upper()]}'


NUMBER_1 = [i for i in input('Введите первое число :')]
NUMBER_2 = [i for i in input('Введите второе число :')]

N1 = Numbers(NUMBER_1)
N2 = Numbers(NUMBER_2)
print(f'Сумма чисел : {N1 + N2}\n'
      f'Произведение чисел : {N1 * N2}')