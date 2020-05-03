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
import timeit

def prime_linear(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, current_prime):
        #OPTIMIZATION
        #for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1
    return current_prime


def prime_eretosfer(num):
    assert num <= 5761455, 'Слишком большой аргумент'
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func:
        if num <= key:
            size = pi_func[key]
            break

    array = [i for i in range(size)]

    array[1] = 0
    for i in range(2, size):
        if array[i] != 0:
            # j = i + i
            j = i ** 2
            while j < size:
                array[j] = 0
                j += i

    res = [i for i in array if i != 0]
    return res[num - 1]


# print(timeit.timeit("prime_linear(10)", setup="from __main__ import prime_linear", number=10))
# print(
#     timeit.timeit(
#         "prime_eretosfer(10)",
#         setup="from __main__ import prime_eretosfer",
#         number=10))

print("Без «Решета Эратосфена» 10: 0.00021493799999999785")
print("Решето Эратосфена 10: 0.000392499000000001")
print("Без «Решета Эратосфена» 100: 0.033897928")
print("Решето Эратосфена 100: 0.007128764000000003")
print("Без «Решета Эратосфена» 1000: 3.697732009")
print("Решето Эратосфена 1000: 0.038735779000000026")

"""При замерах решения Без «Решета Эратосфена»  отработала за 0.00021493799999999785 а 
Решето Эратосфена 0.000392499000000001 секунд, но при увиличении числа алгоритм без «Решета Эратосфена» 
проигровает по скорости потому что имеет сложность  О(n2) a решето O(nlog(log n))"""