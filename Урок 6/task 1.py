from memory_profiler import memory_usage
import sys


# использование памяти зависит еще от типа операционной системы
# для примера list = 40+8*длина
#


def sum(list):  # по памяти данная функция использует только одну переменную sum
    sum = 0
    for i in list:
        sum += i
    print("Памяти израсходавоно " + sys.getsizeof(sum))
    return sum


def func1(arr=[-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]):  # данная функция в худшем случае создаст копию
    # принимающего парметра
    # значит расход памяти равен 40+8*длина
    arr_negative = []
    for i in arr:
        if i < 0:
            arr_negative.append(i)
    return arr_negative


print(sum([1, 2, 3, 4, 5]))

print(memory_usage())
