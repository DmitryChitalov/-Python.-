"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random

def merge_func(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left_lst = lst[:mid]
        right_lst = lst[mid:]

        merge_func(left_lst)
        merge_func(right_lst)

        l_idx, r_idx, or_idx = 0, 0, 0

        for _ in range(len(lst)):
            if l_idx < len(left_lst) and r_idx < len(right_lst):
                if left_lst[l_idx] <= right_lst[r_idx]:
                    lst[or_idx] = left_lst[l_idx]
                    l_idx += 1
                else:
                    lst[or_idx] = right_lst[r_idx]
                    r_idx += 1
                or_idx += 1
            elif l_idx == len(left_lst):
                lst[or_idx] = right_lst[r_idx]
                r_idx += 1
                or_idx += 1
            elif r_idx == len(right_lst):
                lst[or_idx] = left_lst[l_idx]
                l_idx += 1
                or_idx += 1
        return lst


N = int(input('Введите число элементов: '))
SOME_LST = [random.uniform(0, 50) for _ in range(N)]
print(f'Исходный - {SOME_LST}\n'
      f'Отсортированный - {merge_func(SOME_LST)}')
