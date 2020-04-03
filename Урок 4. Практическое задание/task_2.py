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

from math import log1p
from timeit import timeit
from cProfile import run


def pr_classic(number):
    '''
    Классический перебор простых чисел
    для классической реализации сложность O(n^2), тут чуть лучше,
    потому как деление проверял только на простые числа
    '''
    primes = []
    num = 2
    while len(primes) < number:
        for prime in primes:
            if not num % prime:
                break
        else:
            primes.append(num)
        num += 1
    return primes[-1]


def pr_eratosphen(number):
    '''
    необходимая длина исходного массива взята из какой-то статьи
    N * (log1p(N) + log1p(log1p(N)))
    приближается к разпределению простых чисел при больших значениях N,
    так что не самый оптимальный вариант для малых,
    но для локальной задачи норм
    Для решета сложность O(n*lnln(n))), сам не считал,
    в разных источника по разному
    '''
    num = int(number * (log1p(number) + log1p(log1p(number))))
    primes = {6 * k + 1: 1 for k in range(1, num // 6)}
    primes.update({6 * k + 5: 1 for k in range(num // 6)})
    primes[2], primes[3] = 2, 3
    i = 5
    while i * i < num:
        if i in primes:
            for j in range(i * i, num, 2 * i):
                if j in primes:
                    del primes[j]
        i += 2
    return sorted(list(primes.keys()))[N - 1]


SETUP_CL = 'from __main__ import pr_classic, N'
SETUP_ER = 'from __main__ import pr_eratosphen, N'

N = 10
print(timeit('pr_classic(N)', setup=SETUP_CL, number=100))
print(timeit('pr_eratosphen(N)', setup=SETUP_ER, number=100))
print(f'{N}е по счету число (классический): {pr_classic(N)}')  # для проверки
print(f'{N}е по счету число (Эратосфен): {pr_eratosphen(N)}')  # для проверки


N = 100
print(timeit('pr_classic(N)', setup=SETUP_CL, number=100))
print(timeit('pr_eratosphen(N)', setup=SETUP_ER, number=100))
print(f'{N}е по счету число (классический): {pr_classic(N)}')  # для проверки
print(f'{N}е по счету число (Эратосфен): {pr_eratosphen(N)}')  # для проверки


N = 1000
print(timeit('pr_classic(N)', setup=SETUP_CL, number=100))
print(timeit('pr_eratosphen(N)', setup=SETUP_ER, number=100))
print(f'{N}е по счету число (классический): {pr_classic(N)}')  # для проверки
print(f'{N}е по счету число (Эратосфен): {pr_eratosphen(N)}')  # для проверки

N = 10
run('pr_classic(N)')
run('pr_eratosphen(N)')

N = 100
run('pr_classic(N)')
run('pr_eratosphen(N)')

N = 1000
run('pr_classic(N)')
run('pr_eratosphen(N)')

'''
N = 10
классический: 0.0011215819999999994
Эратосфен: 0.0007820680000000003
10е по счету число (классический): 29
10е по счету число (Эратосфен): 29

N = 100
классический: 0.04074241499999999
Эратосфен: 0.007521484999999994
100е по счету число (классический): 541
100е по счету число (Эратосфен): 541

N = 1000
классический: 3.296626484
Эратосфен: 0.1212365369999997
1000е по счету число (классический): 7919
1000е по счету число (Эратосфен): 7919

N       T(класс)/T(Эратосфен)
10      1.43 раз
100     5.42 раз
1000    27.19 раз
Это больше похоже на O(n^2)/O(n*ln(n)), но это детали, возможно
при бОльших n будет приближаться к O(n^2)/O(n*lnln(n))

Как и ожидалось, получается значительный прирост производительности решета
при увеличении числа N

cProfile для классического алгоритма показывает значение 0 при N = 10,100
для N=1000 0,035с
cProfile для решета показывает 0 значения при N = 10,100
для N=1000 0,001с
что в целом соответсвует измерениям timeit
'''
