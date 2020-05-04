"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
"""
Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
 # 2.	Задача: Посчитать четные и нечетные цифры введенного натурального числа.

def with_cycle(NUMBER):

    NOT_EVEN = 0
    for figure in NUMBER:
        NOT_EVEN += int(figure) % 2

    even = len(NUMBER) - NOT_EVEN
    len_number = len(NUMBER)

def recur(NUMBER):
    def remains(figure):
        return int(figure) % 2

    def not_even(NUMBER):
        if NUMBER == []:
            return 0
        return remains(NUMBER[0]) + not_even(NUMBER[1:])

    NUMBER1 = list(NUMBER)
    even = len(NUMBER1) - not_even(NUMBER1)
    len_number = len(NUMBER1)

NUMBER = '123456789'*100

print(timeit.timeit("with_cycle(NUMBER)", setup="from __main__ import with_cycle,NUMBER", number=1000))
print(timeit.timeit("recur(NUMBER)", setup="from __main__ import recur,NUMBER", number=1000))

# Измеряем время выполнения для разных входных данных
"""
Входные данные: NUMBER = '123456789'
Результат:
Решение с циклом:    0.0033571940002730116
Решение с рекурсией: 0.00822915299795568

Входные данные: NUMBER = '123456789'*10
Результат:
Решение с циклом:    0.01930600199557375
Решение с рекурсией: 0.08976999399601482

Входные данные: NUMBER = '123456789'*100
Результат:
Решение с циклом:    0.17113369599974249
Решение с рекурсией: 1.8322751950036036
"""
#Вывод: решение с рекурсией работает медленнее, чем с циклом

# Попытаемся оптимизировать:
def with_cycle_new(NUMBER):

    NOT_EVEN = 0
    for figure in NUMBER:
        NOT_EVEN += int(figure) % 2

    len_number = len(NUMBER)
    even = len_number - NOT_EVEN

def recur_new(NUMBER):
    def not_even(NUMBER):
        if NUMBER == 0:
            return 0
        return NUMBER%10%2 + not_even(NUMBER//10)

    len_number = len(NUMBER)
    even = len_number - not_even(int(NUMBER))

print(timeit.timeit("with_cycle_new(NUMBER)",
                    setup="from __main__ import with_cycle_new,NUMBER", number=1000))
print(timeit.timeit("recur_new(NUMBER)", setup="from __main__ import recur_new,NUMBER", number=1000))

# Проводим измерения скорости повторно и сравниваем:
# Результат:
# Решение с циклом:     до - 0.179
#                       после - 0.168
# Решение с рекурсией:  до - 1.839
#                       после - 0.652
 # Итак: нам удалось оптимезировать решение с рекурсией и сократить время в ~3 раза
