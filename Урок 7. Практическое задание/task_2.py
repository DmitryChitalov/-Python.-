from random import uniform
import timeit


def merge_sort(args):
    if len(args) > 1:
        center = len(args) // 2
        left = args[:center]
        right = args[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                args[k] = left[i]
                i += 1
            else:
                args[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            args[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            args[k] = right[j]
            j += 1
            k += 1
        return args

size = int(input('Enter number of elemnets: '))
pregen_arr = [uniform(0, 50) for _ in range(size)]

print(f'Pregen array: {pregen_arr} \n'
      f'Sorted array: {merge_sort(pregen_arr)}')
print("Время: ", timeit.timeit(
    "merge_sort(pregen_arr)",
    setup="from __main__ import merge_sort, pregen_arr",
    number=1000))
