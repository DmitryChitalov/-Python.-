"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
from random import randint
from memory_profiler import profile
from pympler import asizeof
from guppy import hpy

@profile
def task_3(l):
    min_el = 0
    max_el = 0
    cnt = 0
    # for el in l[1:]:
    #     cnt += 1
    #     if el < l[min_el]:
    #         min_el = cnt
    #     elif el > l[max_el]:
    #         max_el = cnt
    for el in l:
        if el < l[min_el]:
            min_el = cnt
        elif el > l[max_el]:
            max_el = cnt
        cnt += 1

    print(f'Исходный список:   {l}, минимальный элемент - {l[min_el]}, '
          f'максимальный элемент- {l[max_el]}')
    l[min_el], l[max_el] = l[max_el], l[min_el]
    print(f'Измененный список: {l}')


h = hpy()
l = [randint(-100, 100) for _ in range(50000)]
task_3(l)
print(h.heap())

# В силу того, что список крайне мал - сложно что-то оптимизировать.
# Но возможно, если после вычисления мин. и макс. числа и замены исходного списка
# его необходимо будет хранить - можно преобразовать его в кортеж, хоть и выигрыш по объему данных невелик:
print(asizeof.asizeof(l)) # 121336
l = tuple(l)
print(asizeof.asizeof(l)) # 118344
# Либо же если целью скрипта является разовое вычисление, тогда удалить список
del l
# Так же при использовании среза создается копия списка, по которому проходит цикл
#     38     19.0 MiB      0.4 MiB       for el in l[1:]:
# Если переписать без использования среза, то освобождается часть памяти
#     44     18.6 MiB      0.0 MiB       for el in l: