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
import sys
from memory_profiler import profile


@profile()
def my_slice(a):
    print(sys.getrefcount(a[::-1]))
    print(sys.getsizeof(a[::-1]))
    return a[::-1]


@profile()
def my_reverse(a):
    a = list(a)
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    print(sys.getsizeof(a))
    print(sys.getrefcount(a))
    return "".join(a)


@profile()
def my_recursion(a):
    print(sys.getsizeof(a))
    print(sys.getrefcount(a))
    if len(a) == 1:
        return a
    else:
        return a[-1] + my_recursion(a[:-1])


my_str = "123456789012345678901234567890"

print("Срез:")
print(my_slice(my_str))

print("Список:")
print(my_reverse(my_str))

print("Рекурсия:")
print(my_recursion(my_str))

"""
Количество ссылок на объект a:
my_slice: 1
my_reverse: 3
my_recursion: 12
Размер объекта a в байтах:
my_slice: 79
my_reverse: 376
my_recursion: 79
Выделено памяти на выполнение скрипта:
my_slice: 10.4 MiB
my_reverse: 10.5 MiB
my_recursion: 10.6 MiB
Скрипт my_slice - оптимальный по времени выполнения и по работе с памятью
python 2.7
OS - 64bit
"""