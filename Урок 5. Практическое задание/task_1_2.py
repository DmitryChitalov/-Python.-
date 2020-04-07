from collections import namedtuple



ENTITIES = {}

NUM_ENTITIES = int(input("Количество предприятий: "))

for i in range(NUM_ENTITIES):
    name = input(str( i +1) + '-е предприятие: ')
    ENTITIES[name] = [int(i) for i in input('Введите прибыль \
за I, II, III, IV квартал через пробел: \n').split(" ")]
    

print(ENTITIES, '\n')

TOTAL_PROFIT = 0

for name, profit in ENTITIES.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    TOTAL_PROFIT += sum(profit)

AVG_PROFIT = TOTAL_PROFIT / NUM_ENTITIES
print(f'Средняя прибыль за год для всех предприятий {AVG_PROFIT: .2f} \n')

print('Предприятия, у которых прибыль выше среднего: ')

for name, profit in ENTITIES.items():
    if sum(profit) > AVG_PROFIT:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего: ')

for name, profit in ENTITIES.items():
    if sum(profit) < AVG_PROFIT:
        print(f'{name} - {sum(profit)}')