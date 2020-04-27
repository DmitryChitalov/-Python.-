def sieve_erat(length):
    num = 3
    a = [0]
    a[0] = 2
    while num < length:
        k = 0
        if num % 2 != 0:
            for elem in range(len(a)):
                if num % a[elem] == 0:
                    k += 1
            if k == 0:
                a.append(num)
        num += 1
    print(f"\nВыходные данные")
    for elem in range(len(a)):
        print(a[elem])


m = int(input("Введите длину массива:"))
sieve_erat(m)
