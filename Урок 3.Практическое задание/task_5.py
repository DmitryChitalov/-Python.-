"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
import random
LEN = int(input('Введите длину массива: '))
a = [random.randint(-56, 99) for k in range(LEN)]
print(a)

def neg_index(i,MAX_INDEX):
    if a[i] < 0 and MAX_INDEX == -1:
        MAX_INDEX = i
    elif a[i]<0 and a[i] > a[MAX_INDEX] :
        MAX_INDEX = i
    i += 1
    if i < LEN:
        return neg_index(i, MAX_INDEX)
    if MAX_INDEX == -1:
        print('В массиве нет отрицательных чисел')
    else:
        print(f'Индекс максимального отрицательного числа {MAX_INDEX} и это число: {a[MAX_INDEX]}')



neg_index(0,-1)



