"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursive_proof(number, cnt=1):
    if cnt == number:
        return number
    return cnt + (recursive_proof(number, cnt + 1))


try:
    n = int(input('Введите число: '))
    print('Равенство доказано' if recursive_proof(n) == n * (n + 1) / 2 else
          'Равенство не доказано')
except ValueError:
    print('Необходимо ввести целое число')


# Или если нужно все в одной функции:
def recursive_proof_2(number, cnt=1, res=0):
    if cnt > number:
        return f'Равенство доказано' if res == n * (n + 1) / 2 else \
                'Равенство не доказано'
    return recursive_proof_2(number, cnt + 1, res + cnt)


try:
    n = int(input('Введите число: '))
    print(recursive_proof_2(n))
except ValueError:
    print('Необходимо ввести целое число')
"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursive_proof(number, cnt=1):
    if cnt == number:
        return number
    return cnt + (recursive_proof(number, cnt + 1))


try:
    n = int(input('Введите число: '))
    print('Равенство доказано' if recursive_proof(n) == n * (n + 1) / 2 else
          'Равенство не доказано')
except ValueError:
    print('Необходимо ввести целое число')


# Или если нужно все в одной функции:
def recursive_proof_2(number, cnt=1, res=0):
    if cnt > number:
        return f'Равенство доказано' if res == n * (n + 1) / 2 else \
                'Равенство не доказано'
    return recursive_proof_2(number, cnt + 1, res + cnt)


try:
    n = int(input('Введите число: '))
    print(recursive_proof_2(n))
except ValueError:
    print('Необходимо ввести целое число')
