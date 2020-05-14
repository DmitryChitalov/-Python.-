"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random

def mean_1(LST):
    """Функция поиска медианы массива без сортировки"""
    for i in range(len(LST)):
        n = 0 #счетчик больших элементов
        m = 0 #счетчик меньших элементов
        k = 0 #счетчик равных элементов
        for j in range(len(LST)):
            if LST[j] > LST[i]:
                n += 1
            elif LST[j] < LST[i]:
                m += 1
            elif LST[j] == LST[i] and i != j:
                k += 1
        if abs(n - m) == k:
            mean = LST[i]
            break
    return mean

def mean_2(LST, m):
    """Функция поиска медианы массива с использованием сортировки Шелла"""
    n = len(LST)
    gap = m
    while gap > 0:
        for i in range(gap, n):
            temp = LST[i]
            j = i
            while j >= gap and LST[j - gap] > temp:
                LST[j] = LST[j - gap]
                j -= gap
            LST[j] = temp
        gap //= 2
    print(LST)
    return LST[m]

try:
    m = int(input("Введите m – натуральное число для заполнения массива размером 2m + 1: "))
    LST = [random.randint(-100, 100) for _ in range(2 * m + 1)]
    print(LST)
    print(f"Медиана массива равна {mean_1(LST.copy())}")
    print(f"Медиана массива равна {mean_2(LST.copy(), m)}")
except ValueError:
    print("Неправильный ввод данных")
