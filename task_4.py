"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
def task_four():
    num = 0
    max_el = 0
    a = [2, 2, 3, 4, 4, 4, 5, 6, 7]
    for elem in range(len(a)):
        if a.count(elem) > max_el:
            num = a[elem]
            max_el = a.count(elem)
    print(f"{num} число вхождений {max_el}")


task_four()
