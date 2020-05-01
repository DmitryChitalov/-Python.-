import time

def legacy_timeit(func):
    def tmp(n):
        t = time.time()
        res = func(n)
        print(f"Execution time: {time.time()-t}")
        return res

    return tmp

@legacy_timeit
def prime(num):
    count = 1
    next_num = 2

    while count < num:
        next_num += 1
        for i in range(2, int(next_num ** 0.5) + 1):
            if next_num % i == 0:
                break
        else:
            count += 1
    return next_num

prime(30)
