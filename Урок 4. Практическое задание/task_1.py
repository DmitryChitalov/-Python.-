'''
Примечание: учитывая неточность при замере скорости
 выполнения скриптов, я расширил его циклом на 10 повторений,
 с последующий созданием матрицы из результирующих списков,
 что позволило усреднить результаты (при нескольких выполнениях
 кода гораздо чаще стал выводиться один и тот же результат
 из функции local_analytic). Однако при множественном перезапуске
 15-30 раз, примерно каждые 3-5 раз возврат из функции менялся
 на противоположенный и так же оставался стабильным в течении
 3-5 перезапусков кода. (Если Вы знаете, почему так происходит
 пожалуйста, напишите в комментарии)

Анализ: касательно скорости работы (при очень схожих цифрах после замеров)
 очевидно, что рекурсивная функция работает несколько быстрее,
 однако общим преимуществом обеих функций можно
 назвать преобразование к строчному типу.

Так же стоит отметить что при увеличении предустановленного значения
 (строка 40, закомментированные значения) скорость работы
 рекурсивной функции упала, и она стала чаще фигурировать
 в возврате из local_analityc.

Вывод: для работы с небольшими значениями подходят оба скрипта,
 выделить среди них оптимальный вариант невозможно,
 однако при работе с большими и очень юольшими значениями
 предподчительней остается реверс через цикл.
'''


import timeit


def reverce_func(cutter, text, divider, number):
    if cutter != 0:
        return reverce_func(number // divider,
                            text + str(int((number % divider)
                                           // (divider / 10))),
                            divider * 10, number)
    return f'Reversed preset number: {text}'


def while_func(number):
    text = ''
    cutter = 1
    divider = 10
    tmp_res = 1
    number = number
    while cutter != 0:
        cutter = number // divider
        tmp_res = int((number % divider) // (divider / 10))
        text = f'{text}{str(tmp_res)}'
        divider *= 10
    return f'Reversed preset number: {text}'


def local_analytic(log_matrix):
    sum_a = sum(log_matrix[0])
    sum_b = sum(log_matrix[1])
    if sum_a > sum_b:
        slow_rec = 'After 10 cycles of' \
                   '100,000 repetitions of the code, ' \
                   'recursion was slower.'
        return slow_rec
    else:
        slow_cyle = 'After 10 cycles of ' \
                    '100,000 code repetitions, ' \
                    'the cycle turned out to be slower.'
        return slow_cyle

# tested values:
# 4578357745789654 ** 257497,
# 456784748 * 689745748  * 7458963
# 51 ** 847
# 456784748 * 689745748 ** 457845
preset_num = 2147483647 ** 20000
i = 10
recursive_log = []
cycle_log = []
while i > 0:
    recursive_log.append(
        timeit.timeit(
            "reverce_func",
            setup="from __main__ import reverce_func",
            number=100000)
    )
    cycle_log.append(
        timeit.timeit(
            "while_func",
            setup="from __main__ import while_func",
            number=100000)
    )
    i -= 1
log_matrix = [recursive_log, cycle_log]
print(recursive_log)
print(cycle_log)
print(f'{local_analytic(log_matrix)}')
