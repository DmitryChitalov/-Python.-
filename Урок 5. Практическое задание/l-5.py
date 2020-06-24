from collections import defaultdict


def company():
    company = defaultdict(lambda: [[], ])
    count = int(input('Введите количество предприятий: '))
    for i in range(1, count + 1):
        name = input(f'Введите наименование предприятия {i}: ')
        for j in range(1, 5):
            quarter = int(input(f'Прибыль за {j}-ый квартал = '))
            company[name][0].append(quarter)
    print('company ', company)

    profit_average = 0
    for name in company.keys():
        profit = sum(company[name][0])
        print(f'avg in quantity for {name} is {profit / 4}')
        company[name].append(profit)
        profit_average += profit

    print(f'For all companies in year is {profit_average / len(company)}')


company()
