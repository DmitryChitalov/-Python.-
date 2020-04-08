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


def sum_of_hexadecimals(num_1, num_2):
    len1 = len(num_1)
    len2 = len(num_2)
    d = abs(len1 - len2)
    if len1 > len2:  # выравниваем по длине списки, более коротки дополняем '0'
        n1, n2 = [], ['0'] * d
        n2.extend(num_2)
        n1.extend(num_1)
        max_len = len1
    else:
        n1, n2 = ['0'] * d, []
        n1.extend(num_1)
        n2.extend(num_2)
        max_len = len2
    res_sum = []
    k = 0
    for i in range(max_len - 1, -1, -1):
        s = k + corsp.index(n1[i]) + corsp.index(n2[i])
        k = s // 16
        l = s % 16
        res_sum.append(corsp[l])
        if i == 0 and k > 0:
            res_sum.append(corsp[k])
    res_sum.reverse()
    return res_sum


def mult_of_hexadecimals(n1, n2):
    len1 = len(n1)
    len2 = len(n2)
    line_list = [0] * len1  # список для промежуточных результатов перемножения
    p = 0
    for i in range(len1 - 1, -1, -1):
        t = 0
        line_list[i] = []
        line_list[i].extend(['0'] * p)  # выравнивам по длине списки с промежуточными результатами
        p += 1
        for j in range(len2 - 1, -1, -1):
            s = t + corsp.index(n1[i]) * corsp.index(n2[j])
            t = s // 16
            l = s % 16
            line_list[i].append(corsp[l])
            if j == 0 and t > 0:
                line_list[i].append(corsp[t])
        line_list[i].reverse()
    final_res = line_list[0]
    for i in range(1, len1):  # складываем промежуточные результаты для получения финального ответа
        h = sum_of_hexadecimals(final_res, line_list[i])
        final_res = h
    return final_res


corsp = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
num1 = list(input('Enter first number: ').upper())
num2 = list(input('Enter second number: ').upper())

print(sum_of_hexadecimals(num1, num2))
print(mult_of_hexadecimals(num1, num2))
