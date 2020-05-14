"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import randint


def merge_sort(is_list):
    def merge(left_list, right_list):
        sorted_list = []
        left_list_idx = right_list_idx = 0
        for _ in range(len(left_list) + len(right_list)):
            if left_list_idx < len(left_list) and right_list_idx < len(right_list):
                # Сравниваем первые элементы в начале каждого списка
                if left_list[left_list_idx] <= right_list[right_list_idx]:
                    sorted_list.append(left_list[left_list_idx])
                    left_list_idx += 1
                # Если первый элемент правого подсписка меньше, добавляем его
                # в отсортированный массив
                else:
                    sorted_list.append(right_list[right_list_idx])
                    right_list_idx += 1
            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif left_list_idx == len(left_list):
                sorted_list.append(right_list[right_list_idx])
                right_list_idx += 1
            # Операция наоборот
            elif right_list_idx == len(right_list):
                sorted_list.append(left_list[left_list_idx])
                left_list_idx += 1
        return sorted_list

    # Базовое условие
    if len(is_list) <= 1:
        return is_list
    # Шаг рекурсии
    middle = len(is_list) // 2
    left_list = merge_sort(is_list[:middle])
    right_list = merge_sort(is_list[middle:])
    return merge(left_list, right_list)


num_elements = int(input('Введите число элементов: '))
random_list = [randint(0, 50) for _ in range(num_elements)]
print(f'Исходный - {random_list}\n'
      f'Отсортированный - {merge_sort(random_list)}')
