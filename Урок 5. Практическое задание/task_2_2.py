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


class HexDecNum:
    def __init__(self, num):
        self.hex_num = num
        self._corsp = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
        self._len = len(self.hex_num)

    def __add__(self, other):
        d = abs(self._len - other._len)
        if self._len > other._len:  # выравниваем по длине списки, более коротки дополняем '0'
            n1, n2 = [], ['0'] * d
            n2.extend(other.hex_num)
            n1.extend(self.hex_num)
            max_len = self._len
        else:
            n1, n2 = ['0'] * d, []
            n1.extend(self.hex_num)
            n2.extend(other.hex_num)
            max_len = other._len
        res_sum = []
        k = 0
        for i in range(max_len - 1, -1, -1):
            s = k + self._corsp.index(n1[i]) + self._corsp.index(n2[i])
            k = s // 16
            l = s % 16
            res_sum.append(self._corsp[l])
            if i == 0 and k > 0:
                res_sum.append(self._corsp[k])
        res_sum.reverse()
        return res_sum

    def __mul__(self, other):
        line_list = [0] * self._len
        p = 0
        for i in range(self._len - 1, -1, -1):
            t = 0
            line_list[i] = []  # список для промежуточных результатов перемножения
            line_list[i].extend(['0'] * p)  # выравнивам по длине списки с промежуточными результатами
            p += 1
            for j in range(other._len - 1, -1, -1):
                s = t + self._corsp.index(self.hex_num[i]) * self._corsp.index(other.hex_num[j])
                t = s // 16
                l = s % 16
                line_list[i].append(self._corsp[l])
                if j == 0 and t > 0:
                    line_list[i].append(self._corsp[t])
            line_list[i].reverse()
        final_res = line_list[0]
        for i in range(1, self._len):  # складываем промежуточные результаты для получения финального ответа
            s1 = HexDecNum(final_res)
            s2 = HexDecNum(line_list[i])
            final_res = s1 + s2
        return final_res


num1 = list(input('Enter first number: ').upper())
num2 = list(input('Enter second number: ').upper())
a = HexDecNum(num1)
b = HexDecNum(num2)
c = a + b
d = a * b
print(c)
print(d)
