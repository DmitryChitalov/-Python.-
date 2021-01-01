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



class Hex:
    def __init__(self, x):
        self.list = list(x)
        self.x = str(x)

    def __str__(self):
        return str(self.x)

    def __add__(self, obj):
        return hex(int(self.x, 16) + int(str(obj), 16))[2:].upper()

    def __sub__(self, obj):
        return hex(int(self.x, 16) - int(str(obj), 16))[2:].upper()

    def __mul__(self, obj):
        return hex(int(self.x, 16) * int(str(obj), 16))[2:].upper()



hex1 = Hex('A2')
hex2 = Hex('C4F')
print(hex1 + hex2)
print(hex2 - hex1)
print(hex1 * hex2)

# Я не придумал к чему тут применить collections, а классы - пожалуйста :)