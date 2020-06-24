from collections import deque

count_compuny = int(input('Введите количество предприятий для расчета прибыли: '))
companies = deque([] for _ in range(count_compuny))
# print(companies)
for el in range(count_compuny):
    companies[el].append((input('Введите название предприятия: ')))
    sum_revenue = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
    sum_revenue = list(map(int, sum_revenue))
    companies[el].append(sum(sum_revenue))

sum_revenue = 0
for el in companies:
    sum_revenue += el[1]
sum_revenue /= count_compuny
print(f'Средняя годовая прибыль всех предприятий: {sum_revenue}')
answ_min = [el[0] for el in companies if el[1] < sum_revenue]
answ_max = [el[0] for el in companies if el[1] > sum_revenue]

print(f"Предприятия, с прибылью выше среднего значения: {', '.join(answ_max)}")
print(f"Предприятия, с прибылью выше среднего значения: {', '.join(answ_min)}")
