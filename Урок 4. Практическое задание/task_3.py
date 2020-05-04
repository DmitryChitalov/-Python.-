import time

def legacy_timeit(func):
    def tmp(n):
        t = time.time()
        for i in range(1000):
            res = func(n)
        print(f"Average time: {(time.time()-t)/1000}")
        return res

    return tmp

@legacy_timeit
def sieve(n):
    p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
              5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}
    for key in p_func.keys():
        if n <= key:
            length = p_func[key]
            break
    s = [x for x in range(2, length + 1) if
         x not in [i for sub in [list(range(2 * j, length + 1, j)) for j in range(2, length // 2)] for i in sub]]
    return s[n - 1]

sieve(20)

# Average time: 0.003087822437286377
# Average time: 0.0030162153244018557
# Average time: 0.0030391948223114015

# task_2.sieve(20)"
# 1000 loops, best of 5: 3.17 msec per loop

"""
Декоратор, записывающий время выполнения функции 1000 раз, затем делит время выполнения на 1000 для получения среднего 
показателя. Результат выполнения сопоставим со стандартным методом замера с помощью timeit, совпадает по разрядности и 
сходимости результатов. 
Однако, разница есть для одного компьютера и алгоритма - скорее всего, стандартная функция отбрасывает пиковые значения 
для контроля отклонения, в самописной функции это не предусмотрено.
"""