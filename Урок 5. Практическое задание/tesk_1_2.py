""" решение первого задания через defaultdict """
import collections

ORGANIZATION = collections.defaultdict(list)

try:
    AMOUNT_ORG = int(input('Введите количество предприятий для расчета прибыли: '))
except ValueError:
    print("Ошибка: Вы ввели не число, будет запрошено 2 организации")
    AMOUNT_ORG = 2

while AMOUNT_ORG:
    name = input('Введите название предприятия: ')
    quarts = [int(elem) for elem in input(
        'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()]
    if len(list(quarts)) == 4:
        ORGANIZATION[name] = [elem for elem in quarts]
    else:
        print('Ошибка: введено не 4 значения прибыли!')
        continue
    AMOUNT_ORG -= 1
for elem, idx in ORGANIZATION.items():
    ORGANIZATION[elem] = sum(idx) / 4

TOTAL_YEAR_GAIN = sum(ORGANIZATION.values()) / len(ORGANIZATION)
print(f'Средняя годовая прибыль всех предприятий: {TOTAL_YEAR_GAIN}')
print(f'Предприятия, с прибылью выше среднего значения: '
      f'{" ".join(name for name, val in ORGANIZATION.items() if val > TOTAL_YEAR_GAIN)}')
print(f'Предприятия, с прибылью ниже среднего значения: '
      f'{" ".join(name for name, val in ORGANIZATION.items() if val < TOTAL_YEAR_GAIN)}')
