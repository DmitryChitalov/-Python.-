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
from pympler import asizeof

"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Пример:
Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""


"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
Пример:
32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


@profile
def ascii_print(start, end, step):
    """Вывод символов ASCII
    start - начинать с символа под номером start
    end - заканчивается символом под данным номером
    step - количество выводимых символов в 1 строке
    """
    symbols = ""
    for chr_num in range(start, start + step):
        if chr_num > end:
            break
        symbols += f"{chr_num} - {chr(chr_num)} "
    print(symbols)
    if start < end:
        ascii_print(start + step, end, step)


@profile
def ascii_print_cycle(start, end, step):
    """Вывод символов ASCII
    (для усложнения сперва делалась рекурсия, тут её быстрая переделка под цикл)
    start - начинать с символа под номером start
    end - заканчивается символом под данным номером
    step - количество выводимых символов в 1 строке
    """
    while start < end:
        symbols = ""
        for chr_num in range(start, start + step):
            if chr_num > end:
                break
            symbols += f"{chr_num} - {chr(chr_num)} "
        print(symbols)
        start += step


print(asizeof.asizeof(ascii_print(32, 127, 10)))
print(asizeof.asizeof(ascii_print_cycle(32, 127, 10)))


"""Как в случае с циклом так и в случае с рекурсией расход памяти на первый взляд одинаковый 
22.5 MiB (memory_profiler.profile), 8 (pympler.asizeof), но в случае с рекурсией происходит кратный 
вызов функцией самой себя, соответсвенно расход памяти увеличивается"""


# C:\Users\23rad\AppData\Local\Programs\Python\Python38-32\python.exe "C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py"
# 32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
# 42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
# 52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
# 62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
# 72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
# 82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
# 92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
# 102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
# 112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
# 122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74                                     symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77                                     ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63     22.5 MiB     22.5 MiB   @profile
#     64                             def ascii_print(start, end, step):
#     65                                 """Вывод символов ASCII
#     66                                 start - начинать с символа под номером start
#     67                                 end - заканчивается символом под данным номером
#     68                                 step - количество выводимых символов в 1 строке
#     69                                 """
#     70     22.5 MiB      0.0 MiB       symbols = ""
#     71     22.5 MiB      0.0 MiB       for chr_num in range(start, start + step):
#     72     22.5 MiB      0.0 MiB           if chr_num > end:
#     73     22.5 MiB      0.0 MiB               break
#     74     22.5 MiB      0.0 MiB           symbols += f"{chr_num} - {chr(chr_num)} "
#     75     22.5 MiB      0.0 MiB       print(symbols)
#     76     22.5 MiB      0.0 MiB       if start < end:
#     77     22.5 MiB      0.0 MiB           ascii_print(start + step, end, step)
#
#
# 8
# 32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
# 42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
# 52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
# 62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
# 72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
# 82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
# 92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
# 102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
# 112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
# 122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
# Filename: C:/Users/23rad/YandexDisk/GeekBrains/Факультет Python-разработки/1.3 Алгоритмы и структуры данных на Python. Базовый курс/Python_Algos/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     80     22.5 MiB     22.5 MiB   @profile
#     81                             def ascii_print_cycle(start, end, step):
#     82                                 """Вывод символов ASCII
#     83                                 (для усложнения сперва делалась рекурсия, тут её быстрая переделка под цикл)
#     84                                 start - начинать с символа под номером start
#     85                                 end - заканчивается символом под данным номером
#     86                                 step - количество выводимых символов в 1 строке
#     87                                 """
#     88     22.5 MiB      0.0 MiB       while start < end:
#     89     22.5 MiB      0.0 MiB           symbols = ""
#     90     22.5 MiB      0.0 MiB           for chr_num in range(start, start + step):
#     91     22.5 MiB      0.0 MiB               if chr_num > end:
#     92     22.5 MiB      0.0 MiB                   break
#     93     22.5 MiB      0.0 MiB               symbols += f"{chr_num} - {chr(chr_num)} "
#     94     22.5 MiB      0.0 MiB           print(symbols)
#     95     22.5 MiB      0.0 MiB           start += step
#
#
# 8
#
# Process finished with exit code 0

"""Как в случае с циклом так и в случае с рекурсией расход памяти на первый взляд одинаковый 
22.5 MiB (memory_profiler.profile), 8 (pympler.asizeof), но в случае с рекурсией происходит кратный 
вызов функцией самой себя, соответсвенно расход памяти увеличивается"""
