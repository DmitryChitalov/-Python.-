from random import randint


import random
def quickselect_median(arr, pivot_fn=random.choice):
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(arr, len(arr) / 2 - 1, pivot_fn) +
                      quickselect(arr, len(arr) / 2, pivot_fn))


def quickselect(arr, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке arr (с нулевой базой)
    :param arr: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент arr
    """
    if len(arr) == 1:
        assert k == 0
        return arr[0]

    pivot = pivot_fn(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
    
    
MIN_NUM = 1
MAX_NUM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

array = [randint(MIN_NUM, MAX_NUM) for _ in range(size)]
print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

mediana = quickselect_median(array, pivot_fn=random.choice)
print(mediana)