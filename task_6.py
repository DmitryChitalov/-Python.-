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
def task_six():
    a = [6, 58, 50, 77, 49, 88, 42, 67, 14, 79]
    max_el = a[0]
    min_el = a[0]
    amount = 0
    for elem in range(len(a)):
        if a[elem] > max_el:
            max_el = a[elem]
        if a[elem] < min_el:
            min_el = a[elem]
    if a.index(max_el) < a.index(min_el):
        for elem in range(a.index(max_el) + 1, a.index(min_el)):
            amount += a[elem]
    if a.index(max_el) > a.index(min_el):
        for elem in range(a.index(min_el) + 1, a.index(max_el)):
            amount += a[elem]
    if a.index(max_el) == a.index(min_el):
        print(f"Мах равен min")
    print(f"Массив:{a}\nСумма элементов между {min_el} и  {max_el} равна: {amount}")


task_six()
