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

# ВАРИАНТ 1
from collections import defaultdict, deque


NUMBERS = defaultdict(list)
for i in range(2):
    NUMBER = input(f"Введите {i + 1}-е  шестнадцатеричное число: ")
    NUMBERS[NUMBER] = list(NUMBER)

sum = 0
for value in NUMBERS.values():
    sum += int("".join(value), 16)
sum = list(map(str.upper, hex(sum).lstrip("0x")))

prod = 1
for value in NUMBERS.values():
    prod *= int("".join(value), 16)
prod = list(map(str.upper, hex(prod).lstrip("0x")))

print(f"Сумма чисел: {sum}")
print(f"Произведение чисел: {prod}")


# ВАРИАНТ ООП
class Hex:
    def __init__(self, n):
        self.n = n

    def __add__(self, obj):
        return list(map(str.upper, hex(self.n + obj.n).lstrip("0x")))

    def __mul__(self, obj):
        return list(map(str.upper, hex(self.n * obj.n).lstrip("0x")))

x = int(input("Введите первое  шестнадцатеричное число: "), 16)
a = Hex(x)
y = int(input("Введите второе шестнадцатеричное число: "), 16)
b = Hex(y)

print(f"Сумма: {a + b}")
print(f"Произведение: {a * b}")



# Вариант 3 с deque осилила только сложение

def get_value(num):
    if num in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        return int(num)
    if num in ("A", "B", "C", "D", "E", "F"):
        return ord(num) - ord('A') + 10

def get_numeral(val):
    if 0 <= val <= 9:
        return str(val)
    if 10 <= val <= 15:
        return chr(val + ord('A') - 10)

def sum_base_16(x, y):
    x = deque(x)
    y = deque(y)

    if len(x) > len(y):
        for i in range(len(x) - len(y)):
            y.appendleft("0")
    elif len(x) < len(y):
        for j in range(len(y) - len(x)):
            x.appendleft("0")
    carry = 0
    res = deque()

    for i in range(-1, -(len(x)+1), -1):
        nm_1 = get_value(x[i])
        nm_2 = get_value(y[i])
        res_nm = nm_1 + nm_2 + carry
        if res_nm >= 16:
            carry = 1
            res_nm -= 16
        else:
            carry = 0
        res.appendleft(get_numeral(res_nm))

    if carry == 1:
        res.appendleft("1")

    return res

sum = sum_base_16(input("Введите первое  шестнадцатеричное число: "), input("Введите второе шестнадцатеричное число: "))
print(f"Сумма чисел: {list(sum)}")