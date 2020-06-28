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

# Python 3.8.3, Windows 10 64-разрядная

from memory_profiler import profile


@profile()
def function():
    list_1 = [8, 3, 15, 6, 4, 2]
    list_2 = []

    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            list_2.append(i)

    print('Исходный массив: ', list_1, ', результат: ', list_2)


function()


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     21     13.3 MiB     13.3 MiB   @profile()
#     22                             def function():
#     23     13.3 MiB      0.0 MiB       list_1 = [8, 3, 15, 6, 4, 2]
#     24     13.3 MiB      0.0 MiB       list_2 = []
#     25
#     26     13.3 MiB      0.0 MiB       for i in range(len(list_1)):
#     27     13.3 MiB      0.0 MiB           if list_1[i] % 2 == 0:
#     28     13.3 MiB      0.0 MiB               list_2.append(i)
#     29
#     30     13.3 MiB      0.0 MiB       print('Исходный массив: ', list_1, ', результат: ', list_2)


@profile()
def new_function():
    list_1 = [8, 3, 15, 6, 4, 2]

    list_2 = [i for i, x in enumerate(list_1) if x % 2 == 0]

    print('Исходный массив: ', list_1, ', результат: ', list_2)


new_function()


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     13.3 MiB     13.3 MiB   @profile()
#     36                             def new_function():
#     37     13.3 MiB      0.0 MiB       list_1 = [8, 3, 15, 6, 4, 2]
#     38
#     39     13.3 MiB      0.0 MiB       list_2 = [i for i, x in enumerate(list_1) if x % 2 == 0]
#     40
#     41     13.3 MiB      0.0 MiB       print('Исходный массив: ', list_1, ', результат: ', list_2)


@profile()
def while_metod():
    number = 3254
    even = 0
    odd = 0

    while number > 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        number = number // 10
    print('четных - %d, нечетных - %d' % (even, odd))


while_metod()


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     47     13.3 MiB     13.3 MiB   @profile()
#     48                             def while_metod():
#     49     13.3 MiB      0.0 MiB       number = 3254
#     50     13.3 MiB      0.0 MiB       even = 0
#     51     13.3 MiB      0.0 MiB       odd = 0
#     52
#     53     13.3 MiB      0.0 MiB       while number > 0:
#     54     13.3 MiB      0.0 MiB           if number % 2 == 0:
#     55     13.3 MiB      0.0 MiB               even += 1
#     56                                     else:
#     57     13.3 MiB      0.0 MiB               odd += 1
#     58     13.3 MiB      0.0 MiB           number = number // 10
#     59     13.3 MiB      0.0 MiB       print('четных - %d, нечетных - %d' % (even, odd))


@profile()
def recurcion_metod():
    number = 3254

    def recurcion(number, even=0, odd=0):

        if number == 0:
            return even, odd
        else:
            rec_number = number % 10

            number = number // 10

            if rec_number % 2 == 0:
                even += 1
                return recurcion(number, even, odd)
            else:
                odd += 1
                return recurcion(number, even, odd)

    print(f'четных и нечетных равно: {recurcion(number)}')


recurcion_metod()

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     64     13.3 MiB     13.3 MiB   @profile()
#     65                             def recurcion_metod():
#     66     13.3 MiB      0.0 MiB       number = 3254
#     67
#     68     13.3 MiB      0.0 MiB       def recurcion(number, even=0, odd=0):
#     69
#     70     13.3 MiB      0.0 MiB           if number == 0:
#     71     13.3 MiB      0.0 MiB               return even, odd
#     72                                     else:
#     73     13.3 MiB      0.0 MiB               rec_number = number % 10
#     74
#     75     13.3 MiB      0.0 MiB               number = number // 10
#     76
#     77     13.3 MiB      0.0 MiB               if rec_number % 2 == 0:
#     78     13.3 MiB      0.0 MiB                   even += 1
#     79     13.3 MiB      0.0 MiB                   return recurcion(number, even, odd)
#     80                                         else:
#     81     13.3 MiB      0.0 MiB                   odd += 1
#     82     13.3 MiB      0.0 MiB                   return recurcion(number, even, odd)
#     83
#     84     13.3 MiB      0.0 MiB       print(f'четных и нечетных равно: {recurcion(number)}')


# Не понимаю, почему все 4 функции используют ровно 13.3 Мебибайта памяти, и учитывается только память
# на запуск profile. В самих функциях использования памяти не происходит. Вероятно, что я делаю что-то не так, но
# не понимаю что. Исходя из полученных результатов, с использованием памяти никаких проблем нет, ресурсов тратится
# не много. 
