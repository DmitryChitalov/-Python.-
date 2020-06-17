mass = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
print(
    f'Максимальный отрицательный элемент в данном массиве = {max([el for el in mass if el < 0])}, его индекс {mass.index(max([el for el in mass if el < 0]))}')
