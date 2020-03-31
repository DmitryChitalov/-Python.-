"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import cProfile

# Собственная реализация без "решета"
def simple_number():
    NUMBER = 10000
    WORK_LIST = [0] * NUMBER  # создание массива с n количеством элементов
    for i in range(NUMBER):  # заполнение массива ...
        WORK_LIST[i] = i  # значениями от 0 до n-1

    WORK_LIST[1] = 0

    for el in WORK_LIST:
        if el == 0:
            continue
        else:
            for j in WORK_LIST[el+1:]:
                if j != 0 and j % el == 0:
                    WORK_LIST[j] = 0
    RES_LIST = []
    for el in WORK_LIST:
        if el != 0:
            RES_LIST.append(el)
    print(RES_LIST)
    USER_NUM = int(input(f'Введите порядковый номер простого числа до {len(RES_LIST)-1}: '))
    return RES_LIST[USER_NUM]


cProfile.run('simple_number()')

"""
Результат замера: 
Введите порядковый номер простого числа до 1228: 1000
         1239 function calls in 3.220 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.220    3.220 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1    0.630    0.630    3.220    3.220 eratosfen.py:4(simple_number)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    3.220    3.220 {built-in method builtins.exec}
        1    2.586    2.586    2.586    2.586 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.004    0.004 {built-in method builtins.print}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


# Реализация "Решетом"
def erathosfen():
    n = 10000
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    print(b)
    user_num = int(input(f'Введите порядковый номер простого числа до {len(b)-1}: '))
    return b[user_num]


cProfile.run('erathosfen()')

"""
Результат замера: 
Введите порядковый номер простого числа до 1228: 1000
         1239 function calls in 2.621 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.621    2.621 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1    0.011    0.011    2.621    2.621 training_2.py:4(erathosfen)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    2.621    2.621 {built-in method builtins.exec}
        1    2.608    2.608    2.608    2.608 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.print}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
При сравнении двух алгоритмов было выявлено, что функция, написанная по алгоритму "Решето Эратосфена" работает быстрее 
моей реализацией алгоритма. Особенно это хорошо земетно на больших входных данных. Разница, по моему мнению, 
заключается в том, что в моей реализации более сложные условия отсеивания чисел в каждой итерации цикла, а также 
большее количество условий в принципе.
"""