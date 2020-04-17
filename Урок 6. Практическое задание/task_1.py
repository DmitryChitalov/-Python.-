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


from memory_profiler import profile


@profile()
def my_func():
    try:
        first_char = ord(input("First char - "))
        second_char = ord(input("Second char - "))

        first_char_place = first_char - ord('a') + 1
        second_char_place = second_char - ord('a') + 1

        dif = abs(first_char_place - second_char_place) - 1

        print(f"Place of first char - {first_char_place}")
        print(f"Place of second char - {second_char_place}")
        print(f"Number chars between - {dif}")
    except ValueError:
        print("You entered an incorrect value.")


my_func()


"""
Я проанализировал абсолютно все задания 1-3 уроков и абсолютно у всех нет проблем с памятью.
Соответственно проблематично что-то оптимизировать.
Ниже анализ одного из заданий.

Я считаю задание этого урока не корректным. По моему мнению в заднии должен даваться неоптимизированный код, который
необходимо проанализировать и оптимизировать. А сейчас получается мы дожны выполнить задание ради задания,
да еще и практически сами его придумать.

Line #    Mem usage    Increment   Line Contents
================================================
    20     13.6 MiB     13.6 MiB   @profile()
    21                             def simple():
    22     13.6 MiB      0.0 MiB       try:
    23     13.6 MiB      0.0 MiB           first_char = ord(input("First char - "))
    24     13.6 MiB      0.0 MiB           second_char = ord(input("Second char - "))
    25                             
    26     13.6 MiB      0.0 MiB           first_char_place = first_char - ord('a') + 1
    27     13.6 MiB      0.0 MiB           second_char_place = second_char - ord('a') + 1
    28                             
    29     13.6 MiB      0.0 MiB           dif = abs(first_char_place - second_char_place) - 1
    30                             
    31     13.6 MiB      0.0 MiB           print(f"Place of first char - {first_char_place}")
    32     13.6 MiB      0.0 MiB           print(f"Place of second char - {second_char_place}")
    33     13.6 MiB      0.0 MiB           print(f"Number chars between - {dif}")
    34                                 except ValueError:
    35                                     print("You entered an incorrect value.")
"""
