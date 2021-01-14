"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import memory_profiler
import time

# 
def get_odd_1(value):
    result = []
    for var in range(value):
         if var % 2:
             result.append(var)

def get_odd_2(value):
    return [var for var in range(value) if var % 2]

def get_odd_3(value):
    for num in range(value):
        if num % 2:
            yield num

if __name__ == '__main__':
    value = 10000000
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    get_odd_1(value)
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    print(f"Выполнение get_odd_1 заняло {t2 - t1} сек and {m2[0] - m1[0]} Мб")

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    get_odd_2(value)
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    print(f"Выполнение get_odd_2 заняло {t2 - t1} сек and {m2[0] - m1[0]} Мб")

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    mygenerator = get_odd_3(value)
    for i in mygenerator:
        i
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    print(f"Выполнение get_odd_3 и цикла заняло {t2 - t1} сек and {m2[0] - m1[0]} Мб")

"""
Выполнение get_odd_1 заняло 0.078125 сек and 1.33203125 Мб
Выполнение get_odd_2 заняло 0.046875 сек and 0.00390625 Мб
Выполнение get_odd_1  и цикла заняло 0.0625 сек and 0.0 Мб
С точки зренеия оптимальности времени выполнения генераторное выражение оптимально, однако с точки зрения использования памяти generator - имеет неоспоримые преимущества.
Как я понимаю генераторная (generator) функция выполняется долго из-за цикла, в котором получаются выходные значения.
Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)]
"""