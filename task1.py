from memory_profiler import profile


@profile
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

"""
Line #    Mem usage    Increment   Line Contents
================================================
     4     15.5 MiB     15.5 MiB   @profile
     5                             def sieve_erat(length):
     6     15.5 MiB      0.0 MiB       num = 3                         //Память особо не выделяется, для оптимизации можно
     7     15.5 MiB      0.0 MiB       a = [0]                         //использовать готовые модули и решения решета
     8     15.5 MiB      0.0 MiB       a[0] = 2                        //"Эратросфена"
     9     15.5 MiB      0.0 MiB       while num < length:
    10                                     k = 0
    11                                     if num % 2 != 0:                    
    12                                         for elem in range(len(a)):
    13                                             if num % a[elem] == 0:
    14                                                 k += 1
    15                                         if k == 0:
    16                                             a.append(num)
    17                                     num += 1
    18     15.5 MiB      0.0 MiB       print(f"\nВыходные данные")
    19     15.5 MiB      0.0 MiB       for elem in range(len(a)):
    20     15.5 MiB      0.0 MiB           print(a[elem])
"""