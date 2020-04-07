from collections import namedtuple


ENTERPRISE = namedtuple('ENTERPRISE', 'name q1 q2 q3 q4 year')

NUM_ENTITIES = int(input('Введите количество предприятий для анализа: '))
ENTITIES = [0 for _ in range(NUM_ENTITIES)]
PROFIT_TOTAL = 0
print(ENTITIES, '\n')

for i in range(NUM_ENTITIES):
    name = input(f'Введите название {i+1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    PROFIT_TOTAL += year
    ENTITIES[i] = ENTERPRISE(name, *quarters, year,)
    print(ENTITIES[i], '\n')


AVG_PROFIT = PROFIT_TOTAL / NUM_ENTITIES

LESS_AVG = []
MORE_AVG = []

for i in range(NUM_ENTITIES):

    if ENTITIES[i].year < AVG_PROFIT:
        LESS_AVG.append(ENTITIES[i])

    elif ENTITIES[i].year > AVG_PROFIT:
        MORE_AVG.append(ENTITIES[i])

print(f'\nСредняя годовая прибыль по предприятиям: {AVG_PROFIT: .2f}')

print(f'Предприятия, у которых прибыль ниже среднего: ')
for ent in LESS_AVG:
    print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')

print(f'\nПредприятия, у которых прибыль выше среднего: ')
for ent in MORE_AVG:
    print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')