"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
import random


def cicle():
    count = 0
    while count != 50:
        OPER_TYPE = "*"
        if OPER_TYPE == '0':
            break
        if OPER_TYPE in "+-*/":
            try:
                NUM_1 = random.randint(1, 1000)
                NUM_2 = random.randint(1, 1000)
                if OPER_TYPE == '+':
                    RES = NUM_1 + NUM_2
                if OPER_TYPE == '-':
                    RES = NUM_1 - NUM_2
                if OPER_TYPE == '*':
                    RES = NUM_1 * NUM_2
                if OPER_TYPE == '/':
                    if NUM_2 != 0:
                        RES = NUM_1 / NUM_2
                    else:
                        print("Ошибка. Деление на ноль невозможно")
                        continue
                count += 1

                print(f"Ваш результат {RES}")
            except ValueError:
                print(
                    "Вы вместо трехзначного числа ввели строку (((. Исправьтесь")

        else:
            print(f"Неверная операция. Повторите ввод")
            count += 1


def calc_recurs(count=0):
    """Рекурсия"""
    oper_type = "*"

    if oper_type == '0':
        return "Выход"

    else:
        if oper_type in "+-*/":
            try:
                num_1 = random.randint(1, 1000)
                num_2 = random.randint(1, 1000)
                if oper_type == '+':
                    res = num_1 + num_2
                    print(f"Ваш результат {res}")
                    return calc_recurs()

                elif oper_type == '-':
                    res = num_1 - num_2
                    print(f"Ваш результат {res}")
                    return calc_recurs()

                elif oper_type == '*':
                    res = num_1 * num_2
                    print(f"Ваш результат {res}")
                    count += 1
                    if count != 50:
                        return calc_recurs(count)
                    else:
                        return

                elif oper_type == '/':
                    if b != 0:
                        res = num_1 / num_2
                        print(f"Ваш результат {res}")
                    else:
                        print("Деление на 0 невозможно")
                    return calc_recurs()

            except ValueError:
                print(
                    "Вы вместо трехзначного числа ввели строку (((. Исправьтесь")
                return calc_recurs()

        else:
            print("Введен неверный символ, попробуйте еще раз")
            return calc_recurs()


# print(timeit.timeit("cicle()", setup="from __main__ import cicle", number=1000))
# print(
#     timeit.timeit(
#         "calc_recurs()",
#         setup="from __main__ import calc_recurs",
#         number=1000))

print("50 loops: Цыкл: 0.612703242")
print("50 loops: Рекурсия: 0.673594678")
print("100 loops: Цыкл: 1.322893529")
print("100 loops: Рекурсия: 1.422880295")
print("500 loops: Цыкл: 7.609583397")
print("500 loops: Рекурсия: 6.859202294")

"""При замерах решения с Цыклом функцыя отработала за 0.612703242 секунд а Рекурсия за 0.673594678 потому что 
1 решение(цыкл) имет сложность алгоритма О(n) а второе решение (рекурсия) тоже О(n), и в принцыпе они имеют 
зависимость линеиное при больше повторение цыклов ( 100, 500 раз)"""