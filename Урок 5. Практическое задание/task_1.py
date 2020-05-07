"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict

"""
Функция расчета среднегодовой прибыли всех предприятий
и определения предприятий получивших годовую прибыль
выше и ниже среднегодовой
"""
def calc_average(kwargs):
    """
    :param kwargs:
    :return:
    """
    sum_all = 0
    average = 0.0
    list_more_average = []
    list_little_average = []
    """
    Вычисление среднегодовой прибыли всех предприятий
    """
    for k, val in kwargs.items():
        for element in val:
            sum_all += element
    average = sum_all / 4 / len(kwargs)

    """
    Определение какие предприятия получили годовую прибыль выше и ниже среднегодовой
    прибыли всех предприятий
    """
    for k, val in kwargs.items():
        sum_all = 0
        for element in val:
            sum_all += element
        if sum_all / 4 > average:
            list_more_average.append(k)
        elif sum_all / 4 < average:
            list_little_average.append(k)
    return average, list_more_average, list_little_average


# Создание коллекции с названиями фирм и их прибылью за каждый квартал (всего 4 квартала)
FIRM_DATA = defaultdict(list)
while True:
    try:
        FIRM_COUNTS = int(input('Введите количество предприятий для расчета прибыли:\n'))
        if FIRM_COUNTS < 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print(f'Ошибка ввода количества предприятий.\n'
              f'Необходимо ввести целое положительное число.')
    else:
        while FIRM_COUNTS > 0:
            while True:
                try:
                    FIRM_NAME = input(f'Введите название предприятия:\n')
                    if FIRM_NAME.isdigit():
                        raise IOError
                except (ValueError, TypeError, IOError):
                    print(f'Ошибка ввода названия предприятия.\n'
                          f'Название предприятия не может состоять только из цифр.')
                else:
                    while True:
                        try:
                            FIRM_DATA[FIRM_NAME] = list(map(float, input('Введите через пробел прибыль предприятия'
                                                                         ' за каждый квартал:\n').split()))
                            for key, value in FIRM_DATA.items():
                                if key == FIRM_NAME:
                                    for el in value:
                                        if el < 0 or len(value) < 4:
                                            raise IOError
                        except (ValueError, IOError, TypeError):
                            print(f'Ошибка ввода квартальной прибыли предприятия.\n'
                                  f'Необходимо ввести 4 неотрицательных числа через пробел.')
                        else:
                            break
                FIRM_COUNTS -= 1
                break
        break

print(f'=' * 50)
for key, value in FIRM_DATA.items():
    print(f'Название фирмы: {key}  Прибыль за каждый квартал: {value}')
print(f'=' * 50)
print(f'\nСредняя годовая прибыль всех предприятий за год: {calc_average(FIRM_DATA)[0]:.02f}')
print(f'=' * 50)
print(f'Предприятия, с прибылью выше среднего значения:')
for el in calc_average(FIRM_DATA)[1]:
      print(f'{el}')
print(f'=' * 50)
print(f'Предприятия, с прибылью ниже среднего значения:')
for el in calc_average(FIRM_DATA)[2]:
      print(f'{el}')
print(f'=' * 50)
