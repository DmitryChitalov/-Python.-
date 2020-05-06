import collections

def company(profit):
    sum = float(0)
    for i in profit:
        sum += i
    return sum / len(profit)


count = int(input("Количество компаний: "))
dict = collections.defaultdict(float)

for i in range(count):
    name = input("Введите название компании: ")
    profit_list = [float(input(f"Введите прибыль за {i + 1} квартал: ")) for i in range(4)]
    dict[name] = company(profit_list)



avg_list = [dict[i] for i in dict]
avg_profit = company(avg_list)

print(f"Средняя прибыли по компаниям = {avg_profit}")
for i in dict:
    if dict[i] < avg_profit:
        print(f"У Компании {i} прибыль ниже средней и равна {dict[i]}")
    else:
        print(f"У Компании {i} прибыль выше средней и равна {dict[i]}")


