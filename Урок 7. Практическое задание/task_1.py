from random import randint
import timeit


def bubble_sort(args):
    switched = True
    while switched:
        switched = False
        for i in range(len(args) - 1):
            if args[i] < args[i + 1]:
                args[i], args[i + 1] = args[i + 1], args[i]
                switched = True
    return args

pregen_arr = [randint(-100, 100) for _ in range(25)]
preset_arr = [i for i in range(-100, 100)]
preset_arr.reverse()


print(f'Pregenerated array: {pregen_arr} '
      f'\nSorted array: {bubble_sort(pregen_arr)} \n'
      f'Sorted reversed and preset array: {bubble_sort(pregen_arr)}')

print(timeit.timeit(
    "bubble_sort(pregen_arr)",
    setup="from __main__ import bubble_sort, "
          "pregen_arr",
    number=1000))
print(timeit.timeit(
    "bubble_sort(preset_arr)",
    setup="from __main__ import bubble_sort, "
          "preset_arr", number=1000))


"""
Сильно заболел. Работаю с передышками.
Не смог вылечить прогон отсортированного массива в функции.
Где именно не работает вижу - как исправить не знаю.
"""
