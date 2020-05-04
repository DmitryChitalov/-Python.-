"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import statistics
import random
import copy
import timeit
import copy

def func(a):
    a.sort()
    return a[len(a)//2]

def my_mid(a):
    b = copy.deepcopy(a)
    mid_l = random.choice(b)
    indx_mid = b.index(mid_l)
    b.pop(indx_mid)
    R = []
    L = []

    for i in b:  # делим массив на правую и левую часть
        if i > mid_l:
            R.append(i)
        else:
            L.append(i)
    if len(R) == len(L):
        return mid_l

    elif len(R) < len(L):
        R.append(mid_l)
        mid_l = max(L)
        L.pop(L.index(mid_l))
        while len(R) != len(L): # уравниваем 2 массива
            R.append(mid_l)
            mid_l = max(L)
            L.pop(L.index(mid_l))
        return mid_l

    elif len(R) > len(L):
        L.append(mid_l)
        mid_l = min(R)
        R.pop(R.index(mid_l))
        while len(R) != len(L): # уравниваем 2 массива
            L.append(mid_l)
            mid_l = min(R)
            R.pop(R.index(mid_l))
        return mid_l



# замеры 101
a = [random.randint(-10000, 10000) for _ in range(11)]

print("1__________________")
print(timeit.timeit("func(a)", \
    setup="from __main__ import func, a", number=1000))

print("2_________________")
print(timeit.timeit("my_mid(a)", \
    setup="from __main__ import my_mid, a", number=1000))


a = [random.randint(-100000, 100000) for _ in range(101)]
# замеры 10001

print("1__________________")
print(timeit.timeit("func(a)", \
    setup="from __main__ import func, a", number=1000))

print("2_________________")
print(timeit.timeit("my_mid(a)", \
     setup="from __main__ import my_mid, a", number=1000))
print("3_________________")
print(timeit.timeit("med_all(a)", \
    setup="from __main__ import med_all, a", number=1000))

a = [random.randint(-100000, 100000) for _ in range(1001)]


# замеры 100001

print("1__________________")
print(timeit.timeit("func(a)", \
    setup="from __main__ import func, a", number=1000))
print("2_________________")
print(timeit.timeit("my_mid(a)", \
    setup="from __main__ import my_mid, a", number=1000))
"""
1__________________
1.2399000000003213e-05
2_________________
6.673499999999832e-05
1__________________
0.0024469520000000022
2_________________
0.146323355
1__________________
0.031191161999999995
2_________________
33.163421750999994

моя функция оказалась на много дольше, и с увеличением массива становится дольше

Моя фуункция без сортировки оказалась дольше 
Я массив делил на 2 части и уравнивал их так, что бы медиана была по средине 2 массивов
"""
