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


class Hexdeque(collections.deque):
    def __add__(self, other):
        num = ''
        numother =''
        for i in self:
            num +=i
        num = int(num, 16)

        for i in other:
            numother +=i

        numother= int(numother, 16)

        return hex(num + numother)

    def __mul__(self, other):
        num = ''
        numother = ''
        for i in self:
            num += i
        num = int(num, 16)

        for i in other:
            numother += i

        numother = int(numother, 16)

        return hex(num * numother)


NUM1 = Hexdeque(input('Введите первое шестнадцатеричное число: '))
NUM2 = Hexdeque(input('Введите второе шестнадцатеричное число: '))

print(NUM1)
print(NUM2)

print(NUM2 + NUM1)
print(NUM2 * NUM1)