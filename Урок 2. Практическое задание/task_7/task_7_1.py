"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
COUNT_NUMB = int(input('Введите количество элекментов во множестве: '))
RESULT_1 = 0
RESULT_2 = int(COUNT_NUMB * (COUNT_NUMB + 1) / 2)
COUNT = 0
while COUNT_NUMB > 0:
    COUNT += 1
    RESULT_1 = RESULT_1 + COUNT
    COUNT_NUMB -= 1
if RESULT_1 == RESULT_2:
    print(f'Равенство выполняется!')
else:
    print('Равенство не выполняется')

print(f'{RESULT_1} = {RESULT_2}')