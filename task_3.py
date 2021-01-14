"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(f'Execution time for {function} is {time.perf_counter() - start_time} sec')
        return res
    return wrapped

@time_of_function
def reverse_digits(number):
    rev = str(number % 10)
    if number != 0:
        return rev + reverse_digits(number // 10)
    else:
        return ''    


print(reverse_digits(123))
print

"""
Как решить проблему с многократными вызовами декоратора не нашел.
"""