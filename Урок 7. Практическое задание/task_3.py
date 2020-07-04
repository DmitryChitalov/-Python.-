from random import randint


def medianozator(arr_len, args):
    min_array = []
    i = 0
    x = arr_len // 2
    while x != 0:
        min_array.append(min(args))
        args.remove(min(args))
        x -= 1
        i += 1
    return min_array[-1]


сoefficient = randint(10, 25)
arr_len = (сoefficient * 2) + 1
pregen_arr = [randint(-10, 10) for _ in range(arr_len)]


print(f'Pregen array: {pregen_arr} '
      f'\nMedian is: {medianozator(arr_len,pregen_arr)}')
