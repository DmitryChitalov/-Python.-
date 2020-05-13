"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import timeit


def bubble_sort_no_smart(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for n in range(i):
            if numbers[n] < numbers[n + 1]:
                numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]

    return numbers


def bubble_sort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        flag = True
        for n in range(i):
            if numbers[n] < numbers[n + 1]:
                numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]
                flag = False

        if flag is True:
            break
    return numbers


numbers = [random.randint(-100, 100) for _ in range(10)]
print(numbers)
print(bubble_sort(numbers))

print(timeit.timeit('bubble_sort_no_smart(numbers)',
                    setup='from __main__ import bubble_sort_no_smart, numbers', number=1000))
print(timeit.timeit('bubble_sort(numbers)',
                    setup='from __main__ import bubble_sort, numbers', number=1000))


'''
Цель оптимизации: если за проход по списку не совершается ни одной сортировки,
то происходит завершение операции.
По результатам замеров выяснили, что оптимизация существенно уменьшила
время выполнения алгоритма сортировки "пузырьком":
	-- до оптимизации: 0.0380156
	-- после оптимизации: 0.0070906999999999915
'''
