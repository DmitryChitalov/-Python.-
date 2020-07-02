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
from timeit import timeit


def modify_list(func):
    def wrapper(*args, **kwargs):
        i = kwargs.get('i')
        _list = get_list(i)
        a = func(_list, **kwargs)
        return a[i - 1]

    return wrapper


@modify_list
def eratosfen(input_list, **kwargs):
    _list = input_list[:]
    for divider in _list:
        for divided in _list:
            if divider != divided and divided % divider == 0:
                _list.remove(divided)
    return _list


@modify_list
def linear_simple(input_list, **kwargs):
    """Решение без метода решета Эратосфена, можно передать генератор"""

    simple_list = [2]
    for divider in input_list:
        count = 0
        for divided in simple_list:
            if divider != divided and divider % divided == 0:
                count += 1
        if not count:
            simple_list.append(divider)
    return simple_list[1:]


def get_list(i):  # генерю каждый раз исключительно для тестов
    _len = i * 10
    _list = [item for item in range(2, _len + 1)]
    return _list


if __name__ == '__main__':
    i_elem = 10
    len_list = i_elem * 10
    list_a = [item for item in range(2, len_list + 1)]
    list_f = list_a[:]

print(f"Эратосфен: {eratosfen(i=1)} "
      f"time:{timeit('eratosfen(i=1)', setup='from __main__ import eratosfen', number=100)}")
print(f"Эратосфен: {eratosfen(i=10)} "
      f"time:{timeit('eratosfen(i=10)', setup='from __main__ import eratosfen', number=100)}")
print(f"Эратосфен: {eratosfen(i=100)} "
      f"time:{timeit('eratosfen(i=100)', setup='from __main__ import eratosfen', number=100)}")
print(f"Эратосфен: {eratosfen(i=1000)} t"
      f"ime:{timeit('eratosfen(i=1000)', setup='from __main__ import eratosfen', number=100)}")

print(f"не Эратосфен: {linear_simple(i=1)} "
      f"time:{timeit('linear_simple(i=1)', setup='from __main__ import linear_simple', number=100)}")
print(f"не Эратосфен: {linear_simple(i=10)} "
      f"time:{timeit('linear_simple(i=10)', setup='from __main__ import linear_simple', number=100)}")
print(f"не Эратосфен: {linear_simple(i=100)} "
      f"time:{timeit('linear_simple(i=100)', setup='from __main__ import linear_simple', number=100)}")
print(f"не Эратосфен: {linear_simple(i=1000)} "
      f"time:{timeit('linear_simple(i=1000)', setup='from __main__ import linear_simple', number=100)}")

"""
Время выполнения нелинейно увеличивается в геометрической прогресси
Так как использовался цикл в цикле и линейная генерация списка при каждом запуске функции 
(для исключения посторного использования списка при замере времени)
Сложность сложность алгоритма в фунции решета Эратосфена - квадратичная O(n2) 

Эратосфен:       1й эл.:2    time:0.0004630549992725719
Эратосфен:      10й эл.:29   time:0.00819408399911481   больше предыдущего в 17,6957 раз
Эратосфен:     100й эл.:541  time:0.4674339859993779    больше предыдущего в 57,0453 раз
Эратосфен:    1000й эл.:7919 time:37.721348523000415    больше предыдущего в 80,6988 раз


Тут так же нелинейно увеличивается время выполнения функции
Сложность выполнения - квадратичная O(n2) 
Время выполнения в 1,86 раз больше, чем через решето Эратосфена

не Эратосфен:    1й эл.:2    time:0.0005529139998543542
не Эратосфен:   10й эл.:29   time:0.011635190001470619  больше предыдущего в 21,043399163 раз
не Эратосфен:  100й эл.:541  time:0.6747599000009359    больше предыдущего в 57,99302804 раз
не Эратосфен: 1000й эл.:7919 time:54.80080037800144     больше предыдущего в 81,215259499 раз

При одинаковых условиях, функция с решетом Эратосфена отрабатывает эффективнее
Сложность всего скрипта - квадратичная O(n2)  
"""
