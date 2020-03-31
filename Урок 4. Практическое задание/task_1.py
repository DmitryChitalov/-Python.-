"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from timeit import Timer
from random import randint

"""
Первая функция
"""


def task3_1(n):
    # result = {i: 0 for i in range(2, 10)}
    result = [0 for i in range(2, 10)]
    for i in range(2, n):
        for j in range(2, 10):
            if i % j == 0:
                # value = result.get(j) + 1
                # result.update({i: value})
                result[j - 2] += 1

# task3_1 T(N) = const + N*const -> O(N)


"""
Производим замеры для исходной функции
на различных масштабах
сравниваем полученную О-нотацию
с реальными данными
"""
N = 100
with open("task3_1_opt.txt", "w", encoding="utf8") as file:
    while N < 100:
        t1 = Timer(f"task3_1({N})", "from __main__ import task3_1")
        time = t1.timeit(number=1000)
        file.write(f"{N}\t{time}\n")
        del t1
        N += 100

# результаты, записанные в файле совпадают с исходной линейной оценкой
# графическую интерпритацию можно увидеть в exel файле
# в данной задаче можно оптимизировать способ генерации данных
# Используя вместо словаря генератор списков так как в данном случае
# Тратиться дополнительное время на поиск и замену данных
# N = 4900	time_opt = 4,1084308  time_not_opt = 5.116492899999997


"""
Вторая функция.
Здесь приведены несколько вариантов реализации
для оценки наилучших результатов
+ две второстепенные функции генерации
массивов которые не влияют на оценку времени
исходной функции только на тип данных( список или словарь )
"""


def matrix_min(matrix):

    # min_values = [el for el in matrix[0]]
    # min_values = list(matrix[0])
    min_values = list(matrix.get(0))
    # min_values = matrix[0]
    for string in matrix:
        for i in range(len(string)):
            if string[i] < min_values[i]:
                min_values[i] = string[i]
    return min_values


def matrix_min_dict(matrix):

    min_values = list(matrix[0])
    for item in matrix.items():
        for i in range(len(item)-1):
            if item[i] < min_values[i]:
                min_values[i] = item[i]
    return min_values
# matrix_min T(N) = N + K*N -> O(N^2) if K == N


"""
Наихудший вариант достигается при равенстве K и N 
Тогда затраченное время будет расти пропорционально N^2
Проверим результат на входных данных
"""
#  Генерация рандомной квадратной матрицы

# Как словарь
def new_matrix_dict(n):
    # matrix = []
    matrix = {i: [] for i in range(n)}
    for key in matrix:
        matrix[key] = [randint(0, 100) for i in range(n)]
    return matrix

# Как список списков
def new_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(randint(0, 100))
    return matrix


N = 1
file_name = "matrix_min_dict.txt"
with open(file_name, "w", encoding='utf8') as file:
    while N < 100:
        # tmp_matrix = new_matrix(N)
        tmp_matrix = new_matrix_dict(N)
        t1 = Timer(f"matrix_min_dict({tmp_matrix})", "from __main__ import matrix_min_dict")
        # t1 = Timer(f"matrix_min({tmp_matrix})", "from __main__ import matrix_min")
        time = t1.timeit(number=100)
        file.write(f"{N}\t{time}\n")
        N += 1

"""
Результаты совпадают с исхродным предположением квадратичной зависимости
отклонения от общей тенденции связаны с разницой обработки условия сравнения
Возможная оптимизация:
1)вместо генератора использовать лист
2)Использовать словарь для хранения матрицы
Ухудшение оптимизации:
1)Присвоение списка без генератора
Все результаты см в файле exel или текстовые файлы
У всех вариантов наблюдается квадратичная зависимость 
Однако тенденция роста у всех разная 
Это связано с более оптимизировнными способами генерации данных
"""


# Учитывая полученные данные, можно сделать вывод, что наиболее оптимизированный способ
# Использование листа вместо генератора тогда как простое присвоение
# Ухудшает производимость так же лучше использовать в качестве хранения словарь
# так как он использует хеш-функции, что намного быстрее
# N = 99	time_gen = 0,0531535	time_list = 0,0524669	time_eq = 0,1103767     time_dict_list = 0,0095262

