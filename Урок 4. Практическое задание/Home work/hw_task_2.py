from timeit import Timer

def perebioer(i):
    count = 1
    num = 2
    while count <= i:
        proverk = 1
        prost = True
        while proverk <= num:
            if num % proverk == 0 and proverk != 1 and proverk != num:
                prost = False
                break
            proverk += 1
        if prost:
            if count == i:
                break
            count += 1
        num += 1
    return num


def eratosfen(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]

i = 10

timer_1 = Timer('perebioer(i)', 'from __main__ import perebioer, i')
print(f'Perebioer funk {timer_1.timeit(number=100)} ')
timer_2 = Timer('eratosfen(i)', 'from __main__ import eratosfen, i')
print(f'Eratosfen funk {timer_2.timeit(number=100)} ')
#print(perebioer(100))
#print(eratosfen(100))

'''
При i = 10
Perebioer funk 0.002182200000000002 
Eratosfen funk 0.3914909 

При i = 100
Perebioer funk 0.2595295 
Eratosfen funk 0.39172470000000004 

При i = 1000
Perebioer funk 43.3965657 
Eratosfen funk 0.3916795000000022 

Алгоритм с «Решето Эратосфена» в разы быстрее на огромных вычислениях,
 но при малом объёме данных он проигрывает по скорости выполнения.
 Нашёл в интернете сложность «Решето Эратосфена»: O(NloglogN)
 Сам не знаю как оценить, так как есть логическое ветвление...
'''