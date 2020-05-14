"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randint

m = int(input("Введите m = "))
arr_len = 2 * m + 1
print("Длина массива 2m + 1 =", arr_len)
array = [randint(-100, 100) for i in range(arr_len)]
print("Несортированный массив:", array, sep="\n\t")

def partition(array, left, right):
    if left != right:
        rnd = randint(0, right - left)
        array[left + rnd], array[right] = array[right], array[left + rnd]
    val = array[right]
    i = left - 1
    for j in range(left, right + 1):
        if array[j] <= val:
            i += 1
            array[i], array[j] = array[j], array[i]
    return i

def find_order(array, idx):
    left = 0
    right = len(array) - 1
    while True:
        mid = partition(array, left, right)
        if mid < idx:
            left = mid + 1
        elif mid > idx:
            right = mid - 1
        else:
            return array[idx]

print("Медианное значение:", find_order(array, m), sep="\n\t")

#print("Проверка с использованием встроенной сортировки:")
#array.sort()
#print("Медианное значение:", array[m], sep="\n\t")



