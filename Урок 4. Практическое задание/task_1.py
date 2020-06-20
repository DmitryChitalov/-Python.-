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
"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
from random import randint
import timeit


def min_max(l):
    min_el = l[0]
    cnt = 0
    second_el = 50
    for el in l:
        if el == min_el:
            cnt += 1
        elif el < min_el:
            min_el, second_el = el, min_el
            cnt = 1
        elif second_el > el > min_el:
            second_el = el
    if cnt >= 2:
        return f'Исходный массив: {l}\nНаименьший элемент: ' \
               f'{min_el} встречается в этом массиве {cnt} раз\n'
    else:
        return f'Исходный массив: {l}\nНаименьший элемент: {min_el},\n' \
               f'Второй наименьший элемент: {second_el}'


my_list_10 = [randint(-50, 50) for _ in range(10)]
my_list_100 = [randint(-50, 50) for _ in range(100)]
my_list_1000 = [randint(-50, 50) for _ in range(1000)]
print('Не оптимизированная функция min_max')
print(f'{timeit.timeit("min_max(my_list_10)", setup="from __main__ import min_max, my_list_10", number=1000)} - 10 элементов')
print(f'{timeit.timeit("min_max(my_list_100)", setup="from __main__ import min_max, my_list_100", number=1000)} - 100 элементов')
print(f'{timeit.timeit("min_max(my_list_1000)", setup="from __main__ import min_max, my_list_1000", number=1000)} - 1000 элементов')


def min_max_optimized(l):
    min_el = min(l)
    cnt = l.count(min_el)
    if cnt > 1:
        return f'Исходный массив: {l}\nНаименьший элемент: ' \
               f'{min_el} встречается в этом массиве {cnt} раз\n'
    else:
        s = set(l)
        return f'Исходный массив: {l}\nНаименьший элемент: {min_el},\n' \
               f'Второй наименьший элемент: {sorted(s)[1]}'
print('Оптимизированная функция min_max_optimized')
print(f'{timeit.timeit("min_max_optimized(my_list_10)", setup="from __main__ import min_max_optimized, my_list_10", number=1000)} - 10 элементов')
print(f'{timeit.timeit("min_max_optimized(my_list_100)", setup="from __main__ import min_max_optimized, my_list_100", number=1000)} - 100 элементов')
print(f'{timeit.timeit("min_max_optimized(my_list_1000)", setup="from __main__ import min_max_optimized, my_list_1000", number=1000)} - 1000 элементов')

# Аналитика:
# При увеличении размера массива на порядок прямопропорционально увеличивается
# на порядок время выполнения при неоптимизированном исполении:
# 0.003061972000000003 - 10 элементов
# 0.020813995999999998 - 100 эл.
# 0.202655094 -  1000 эл.
# После оптимизации и использования встроенных функций min, count, set, sorted
# на минимальных массивах практически нет разницы по времени выполнения,
# но чем массив больше, чем выше выигрыш по скорости,
# потому что мы проходим весь список не через цикл, а встроенными быстрыми функциями
# 0.0035254680000000316 - 10
# 0.01321794599999998 - 100
# 0.125324282 - 1000 эл.

"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

def num_counter(n, l):
    res = 0
    for el in l:
        while el != 0:
            if el % 10 == n:
                res += 1
            el //= 10
    return f'Было введено {res} цифр "{n}"'

my_list_10 = [randint(0, 5000) for _ in range(10)]
my_list_100 = [randint(0, 5000) for _ in range(100)]
my_list_1000 = [randint(0, 5000) for _ in range(1000)]
num = randint(0, 9)

print('Не оптимизированная функция num_counter')
print(timeit.timeit("num_counter(num, my_list_10)", setup='from __main__ import num_counter, num, my_list_10', number=1000))
print(timeit.timeit("num_counter(num, my_list_100)", setup='from __main__ import num_counter, num, my_list_100', number=1000))
print(timeit.timeit("num_counter(num, my_list_1000)", setup='from __main__ import num_counter, num, my_list_1000', number=1000))

def num_counter_opt(n, l):
    res = 0
    n = str(n)
    for el in l:
        res += str(el).count(n)
    return f'Было введено {res} цифр "{n}"'

print('Оптимизированная функция num_counter_opt')
print(timeit.timeit("num_counter_opt(num, my_list_10)", setup='from __main__ import num_counter_opt, num, my_list_10', number=1000))
print(timeit.timeit("num_counter_opt(num, my_list_100)", setup='from __main__ import num_counter_opt, num, my_list_100', number=1000))
print(timeit.timeit("num_counter_opt(num, my_list_1000)", setup='from __main__ import num_counter_opt, num, my_list_1000', number=1000))

# Аналитика:
# Для удобства вычисления был убран ручной ввод с клавиатуры.
# При увеличении массива примерно на порядок увеличивается время выполнения:
# 0.005143688000000035 - 10 элементов
# 0.045882701000000026 - 100 эл.
# 0.464994971 -  1000 эл.
# Из-за того, что в оптимизированной функции нет вложенного цикла, а поиск вхождений идет через метод count -
# выигрыш о размеров массива не больше 0.1 на 1000 элементов:
# 0.00524789399999992 - - 10
# 0.03380094999999994 - 100
# 0.3400999279999999 - 1000 эл.
# Однако, при увеличении порядка самих чисел в массиве за счет того, что не проводятся вычисления во вложенном цикле -
# достигается максимальный результат:
# my_list = [randint(0, 5000000) for _ in range(1000)]
# print(timeit.timeit("num_counter(num, my_list)", setup='from __main__ import num_counter, num, my_list', number=1000))
# print(timeit.timeit("num_counter_opt(num, my_list)", setup='from __main__ import num_counter_opt, num, my_list', number=1000))
# 0.852849975  против 0.352844554, более чем в два раза, примечательно, что хоть и числа и увеличились на 3 порядка,
# но время выполнения с использованием метода count - осталось практически тем же.

"""
3.    Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

try:
    user_number = int(input('Введите целое число: '))
    res = ''
    while user_number != 0:
        res += str(user_number % 10)
        user_number //= 10
    print(f'Перевернутое число: {res}')
except ValueError:
    print('Необходимо ввести целое число')


"""



