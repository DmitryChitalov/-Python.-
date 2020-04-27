"""
решето Эратосфена
"""

n = int(input("вывод простых чисел до числа ... "))


def f_sieve(lenghth):
    empty_sieve = [0] * lenghth
    return empty_sieve


def fil_sieve(full_sieve, lenghth):
    for i in range(lenghth):
        full_sieve[i] = i
    full_sieve[1] = 0
    return full_sieve


def filter_sieve(sieve, lenghth):
    number = 2
    while number < lenghth:
        if sieve[number] != 0:
            next_number = number * 2
            while next_number < lenghth:
                sieve[next_number] = 0
                next_number = next_number + number
        number += 1
    return sieve


def eratosphen(lenghth):
    lenghth += 1
    sieve = f_sieve(lenghth)
    sieve = fil_sieve(sieve, lenghth)
    sieve = filter_sieve(sieve, lenghth)
    result = [x for x in sieve if sieve[x] != 0]
    return result


print(eratosphen(n))
