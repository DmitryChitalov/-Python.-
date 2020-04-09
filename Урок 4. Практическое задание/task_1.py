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

from timeit import Timer


USER_RANGE = 10
MY_ARRAY = [i for i in range(2, USER_RANGE)]

def multiplicity():
    for i in range(2, 10):
        MULTIPLE = 0
        for j in MY_ARRAY:
            if j % i == 0:
                MULTIPLE += 1

"""
Сложность текущего алгоритма - линейная, т.к. при увеличении входных данных, 
увеличивается только вложенный цикл j. Цикл i всегда выполняется 9 раз
"""

t1 = Timer("multiplicity()", "from __main__ import multiplicity")
print(f"При входных данных {USER_RANGE}, функция 1 выполнилась за {t1.timeit(number=10000)} секунд")
USER_RANGE = 20
MY_ARRAY = [i for i in range(2, USER_RANGE)]
print(f"При входных данных {USER_RANGE}, функция 1 выполнилась за {t1.timeit(number=10000)} секунд")
USER_RANGE = 30
MY_ARRAY = [i for i in range(2, USER_RANGE)]
print(f"При входных данных {USER_RANGE}, функция 1 выполнилась за {t1.timeit(number=10000)} секунд")
USER_RANGE = 40
MY_ARRAY = [i for i in range(2, USER_RANGE)]
print(f"При входных данных {USER_RANGE}, функция 1 выполнилась за {t1.timeit(number=10000)} секунд")


"""
Сложность алгоритма - квадратичная, так как теперь увеличивается и цикл i, и цикл j.
И в итоге при увеличении входных данных, время выполнения увеличивается нелинейно.
"""

USER_RANGE = 10


def multiplicity_2():
    for i in range(2, USER_RANGE):
        MULTIPLE = 0
        for j in MY_ARRAY:
            if j % i == 0:
                MULTIPLE += 1


t2 = Timer("multiplicity_2()", "from __main__ import multiplicity_2")
print(f"При входных данных {USER_RANGE}, функция 2 выполнилась за {t2.timeit(number=10000)} секунд")
USER_RANGE = 20
MY_ARRAY = [i for i in range(2, USER_RANGE)]
print(f"При входных данных {USER_RANGE}, функция 2 выполнилась за {t2.timeit(number=10000)} секунд")
USER_RANGE = 30
MY_ARRAY = [i for i in range(2, USER_RANGE)]
print(f"При входных данных {USER_RANGE}, функция 2 выполнилась за {t2.timeit(number=10000)} секунд")
USER_RANGE = 40
MY_ARRAY = [i for i in range(2, USER_RANGE)]
print(f"При входных данных {USER_RANGE}, функция 2 выполнилась за {t2.timeit(number=10000)} секунд")


"""
Попробуем оптимизировать задачу на переворот числа
"""
USER_NUMBER = 8237


def number_converter(number):
    converted_number = ""
    while number != 0:
        converted_number = converted_number + str(number % 10)
        number = number // 10
    return converted_number


t3 = Timer("number_converter(USER_NUMBER)", "from __main__ import number_converter, USER_NUMBER")
print(f"{t3.timeit()} секунд выполнялась функция при конкатинации")


def number_converter_2(number):
    converted_number = str(number)[::-1]
    return converted_number


t4 = Timer("number_converter_2(USER_NUMBER)", "from __main__ import number_converter_2, USER_NUMBER")
print(f"{t4.timeit()} секунд выполнялась функция при использовании слайса")

"""
При использовании среза, операция занимает намного меньше времени, так как
конкатинация получается намного тяжелее (не нашел информации о сложности операции конкатинации)
При использовании среза, сложность становится линейной O(n), где n - длина среза
"""