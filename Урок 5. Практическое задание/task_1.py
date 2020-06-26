from collections import namedtuple


# Request and fill profit function.
def profit_setter(n, q):
    tmp = float(input(f'Enter the profit '
                f'of the {n + 1} company '
                f'for the {q} quarter: '))
    return tmp


"""
Понимаю, что следовало бы сделать функцию атомарной,
однако при выполнении функцией строго одной задачи
пришлось бы пересоздавать несколько раз именнованный(-е) 
кортеж(-и) для передачи его(их) в другую(-ие) функцию(-ии).
"""


def average_moreless(args):
    year_prof = list()
    successful_companies = list()
    unsuccessful_companies = list()
    tmp_summ = 0
    tmp = 0
    for el in args:
        tmp_summ = sum(el[3:])
        year_prof.append(tmp_summ)
    average = (sum(year_prof) / args[tmp].ttl)
    for el in year_prof:
        if el > average:
            successful_companies.append(args[tmp].name)
            tmp += 1
        else:
            unsuccessful_companies.append(args[tmp].name)
            tmp += 1
    text_1 = f'Companies whose ' \
             f'annual profit was above ' \
             f'average: {" ".join(map(str, successful_companies))}.'
    text_2 = f'Companies whose ' \
             f'profit for the year was below ' \
             f'average: {" ".join(map(str, unsuccessful_companies))}.'
    return print(text_1, '\n', text_2, sep='')

# Preset tuple, cutter and n settings
default = namedtuple('Companies', 'id ttl name q1 q2 q3 q4')
cutter = int(input('Enter the number of companies: '))
matrix_of_companies = []
n = 0


# The cycle of requesting company data.
while not n == cutter:
    user_data = default(
        id=n+1,
        ttl=cutter,
        name=str(input(f'Enter name of {n + 1} company: ')),
        q1=profit_setter(n, 1),
        q2=profit_setter(n, 2),
        q3=profit_setter(n, 3),
        q4=profit_setter(n, 4)
    )
    matrix_of_companies.append(user_data)
    n += 1


average_moreless(matrix_of_companies)
