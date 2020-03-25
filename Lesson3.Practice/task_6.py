"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
from random import randint


def get_array(count):
    """
    Генерация случайного массива
    """
    for i in range(EL_COUNT):
        LST.append(randint(1, 100))
    return LST


def get_sum_el(max=0, min=999, min_ind=0, max_ind=0, result=0):
    """
    В одномерном массиве найти сумму элементов,
    находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать.
    """
    arr = get_array(EL_COUNT)
    print(arr)
    for count in range(len(arr)):
        if arr[count] > max:
            max = arr[count]
            max_ind = count
        if arr[count] < min:
            min = arr[count]
            min_ind = count
    if max_ind > min_ind:
        for cnt in range(len(arr)):
            while min_ind < cnt < max_ind:
                result += arr[cnt]
                cnt += 1
            if cnt == max_ind:
                break
    else:
        for cnt in range(len(arr)):
            while max_ind < cnt < min_ind:
                result += arr[cnt]
                cnt += 1
            if cnt == min_ind:
                break
    return f'Сумма элементов между минимальным {min}  и максимальным {max} элементами: {result}'






if __name__ == '__main__':
    LST = []
    try:
        EL_COUNT = int(input("Введите количество  элементов в массиве: "))
        if EL_COUNT < 0:
            print("Количество элементов должно быть неотрицательным")
        else:
            print(get_sum_el())
    except ValueError:
        print("Ошибка ввода значения")
