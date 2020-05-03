count = int(input("Enter size = "))


# функция algo имеет квадратичную сложность O(n^2) ведь чем больще число, тем больше сложность у функции IsPrime,
# а по-скольку надо проверять каждое число то мы проверяем n раз функцию IsPrim, котрая сама O(n)
def algo(count):
    i = 2
    while True:
        if IsPrime(i) == True:
            count -= 1
            i += 1
            if count == 0:
                return i - 1
        else:
            i += 1


# функция IsPrime имеет линейную сложность O(n) - где n - число, которое проверяем на прстоту
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def eratosthenes(n):
    # O(nlog(n))
    # через математичеое доказательство
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


print(algo(count))
list = eratosthenes(count*10)
list_prime = []
a = 0
for i in list:
    if i != 0:
        list_prime.append(i)
print(list_prime[count-1])




