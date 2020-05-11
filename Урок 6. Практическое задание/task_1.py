"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile
import random

"""
Ниже результаты измерений различных заданий и вариантов решения. В целом, у меня вообще не получается "нагрузить" сильно
память - даже по варианту (Memory_check_2), разобранный на уроке у меня получаются другие числа. 
Как я понимаю, это зависит от способностей компьютера или ОС? Инкримент везде 0, что, как я понимаю, 
говорит о слишком малых значениях, которые не дают нагрузку на память
Хорошая нагрузка и показательные результаты дал последний эксперимент, при задании массива случайных числе из 
стотысячного интервала. Чем больше интервал, тем больше "думает" компьютер и больше нагрузка на память.

В первом примере ожидала сильного отличия между циклом и рекурсией в пользу рекурсии по нагрузке памяти, однако на моих 
примерах рекурсия была не хуже по памяти. Думаю, что если бы были более сложные вычисления, то рекурсия бы заняла больше 
памяти

У меня 64-разрядная MacOS.
Версия Python: Python 3.8.0
"""


# Исследования:

# Task 1.1 (lesson 1):
# Вариант 1(цикл):
"""
@profile
def count():
    while True:
        oper = input("Введите операцию (+, -, *, /) или нажмите 0 для выхода из программы: ")
        if oper == '0':
            return ("Завершение программы")
        elif oper == '+' or oper == '-' or oper == '/' or oper == '*':
            numb1 = int(input("Введите первое число: "))
            numb2 = int(input("Введите второе число: "))
            if oper == '+':
                print(numb1 + numb2)
            elif oper == '-':
                print(numb1 - numb2)
            elif oper == '/':
                print(numb1 / numb2)
            elif oper == '*':
                print(numb1 * numb2)
        else:
            print("Вы ввели ввели неверный знак")

print(count())
"""

"""
Результат измерений Варианта 1 (цикл):

Line #    Mem usage    Increment   Line Contents
================================================
    33     11.2 MiB     11.2 MiB   @profile
    34                             def count():
    35                                 while True:
    36     11.2 MiB      0.0 MiB           oper = input("Введите операцию (+, -, *, /) или нажмите 0 для выхода из программы: ")
    37     11.2 MiB      0.0 MiB           if oper == '0':
    38     11.2 MiB      0.0 MiB               return ("Завершение программы")
    39     11.2 MiB      0.0 MiB           elif oper == '+' or oper == '-' or oper == '/' or oper == '*':
    40     11.2 MiB      0.0 MiB               numb1 = int(input("Введите первое число: "))
    41     11.2 MiB      0.0 MiB               numb2 = int(input("Введите второе число: "))
    42     11.2 MiB      0.0 MiB               if oper == '+':
    43                                             print(numb1 + numb2)
    44     11.2 MiB      0.0 MiB               elif oper == '-':
    45                                             print(numb1 - numb2)
    46     11.2 MiB      0.0 MiB               elif oper == '/':
    47     11.2 MiB      0.0 MiB                   print(numb1 / numb2)
    48     11.2 MiB      0.0 MiB               elif oper == '*':
    49     11.2 MiB      0.0 MiB                   print(numb1 * numb2)
    50                                     else:
    51                                         print("Вы ввели ввели неверный знак")


"""

"""
# Вариант 2 (рекурсия):

@profile
def recursecount():
    oper = input("Введите операцию (+, -, *, /) или нажмите 0 для выхода из программы: ")
    if oper == '0':
        return ("Завершение программы")
    elif oper == '+' or oper == '-' or oper == '/' or oper == '*':
        numb1 = int(input("Введите первое число: "))
        numb2 = int(input("Введите второе число: "))
        if oper == '+':
            print(numb1 + numb2)
        elif oper == '-':
            print(numb1 - numb2)
        elif oper == '/':
            print(numb1 / numb2)
        elif oper == '*':
            print(numb1 * numb2)
        return recursecount()
    else:
        print("Вы ввели ввели неверный знак")
        return recursecount()

print(recursecount())
"""

"""
Результаты измерений Варианта 2 (рекурсия):

Line #    Mem usage    Increment   Line Contents
================================================
    67     10.9 MiB     10.9 MiB   @profile
    68                             def recursecount():
    69     10.9 MiB      0.0 MiB       oper = input("Введите операцию (+, -, *, /) или нажмите 0 для выхода из программы: ")
    70     10.9 MiB      0.0 MiB       if oper == '0':
    71     10.9 MiB      0.0 MiB           return ("Завершение программы")
    72     10.9 MiB      0.0 MiB       elif oper == '+' or oper == '-' or oper == '/' or oper == '*':
    73     10.9 MiB      0.0 MiB           numb1 = int(input("Введите первое число: "))
    74     10.9 MiB      0.0 MiB           numb2 = int(input("Введите второе число: "))
    75     10.9 MiB      0.0 MiB           if oper == '+':
    76     10.9 MiB      0.0 MiB               print(numb1 + numb2)
    77     10.9 MiB      0.0 MiB           elif oper == '-':
    78                                         print(numb1 - numb2)
    79     10.9 MiB      0.0 MiB           elif oper == '/':
    80     10.9 MiB      0.0 MiB               print(numb1 / numb2)
    81                                     elif oper == '*':
    82                                         print(numb1 * numb2)
    83     10.9 MiB      0.0 MiB           return recursecount()
    84                                 else:
    85     10.9 MiB      0.0 MiB           print("Вы ввели ввели неверный знак")
    86     10.9 MiB      0.0 MiB           return recursecount()

"""

# Task 1 (Lesson 4):

"""

# Вариант 1

m = 0
num = 0
array = [random.randint(0, 10) for el in range(10)]

@profile
def func_1():
    global m, num
    # print(array)
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return (f'Чаще всего встречается число {num}, оно появилось в массиве {m} раз(а)')


func_1()

# Вариант 2. Решение через ф-ю max (Мое):

elem = 0

@profile
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    # print(new_array)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return (f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)')


func_2()

# Вариант 3. Решение через ф-ю max (Преподаватель):
@profile
def func_3():
    # print(array)
    numb = max(array, key=array.count)
    return (f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)")


func_3()

Результаты измерений:

Вариант 1:

Line #    Mem usage    Increment   Line Contents
================================================
   123     11.1 MiB     11.1 MiB   @profile
   124                             def func_1():
   125                                 global m, num
   126                                 # print(array)
   127     11.1 MiB      0.0 MiB       m = 0
   128     11.1 MiB      0.0 MiB       num = 0
   129     11.1 MiB      0.0 MiB       for i in array:
   130     11.1 MiB      0.0 MiB           count = array.count(i)
   131     11.1 MiB      0.0 MiB           if count > m:
   132     11.1 MiB      0.0 MiB               m = count
   133     11.1 MiB      0.0 MiB               num = i
   134     11.1 MiB      0.0 MiB       return (f'Чаще всего встречается число {num}, оно появилось в массиве {m} раз(а)')
   
   
Вариант 2:

Line #    Mem usage    Increment   Line Contents
================================================
   143     11.2 MiB     11.2 MiB   @profile
   144                             def func_2():
   145     11.2 MiB      0.0 MiB       new_array = []
   146     11.2 MiB      0.0 MiB       for el in array:
   147     11.2 MiB      0.0 MiB           count2 = array.count(el)
   148     11.2 MiB      0.0 MiB           new_array.append(count2)
   149                                 # print(new_array)
   150     11.2 MiB      0.0 MiB       max_2 = max(new_array)
   151     11.2 MiB      0.0 MiB       elem = array[new_array.index(max_2)]
   152     11.2 MiB      0.0 MiB       return (f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)')
  
Вариант 3:
 
   Line #    Mem usage    Increment   Line Contents
================================================
   158     11.2 MiB     11.2 MiB   @profile
   159                             def func_3():
   160                                 # print(array)
   161     11.2 MiB      0.0 MiB       numb = max(array, key=array.count)
   162     11.2 MiB      0.0 MiB       return (f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)")

"""

# Task 3 (lesson 3):

"""
import random

@profile
def arr():
    array = [random.randint(-100, 100) for i in range(100000)]
    print(array)
    max1 = max(array)
    min1 = min(array)
    print(f'Максимальное число в массиве: {max1}')
    print(f'Минимальное число в массиве: {min1}')
    a = array.index(min1)
    b = array.index(max1)
    array.remove(min1)
    array.remove(max1)
    array.insert(a, max1)
    array.insert(b, min1)
    return (f"Новый массив: {array}")


print(arr())
"""
"""
Результаты измерений:

Line #    Mem usage    Increment   Line Contents
================================================
   244     11.3 MiB     11.3 MiB   @profile
   245                             def arr():
   246     13.2 MiB      0.1 MiB       array = [random.randint(-100, 100) for i in range(100000)]
   247     14.6 MiB      1.4 MiB       print(array)
   248     14.6 MiB      0.0 MiB       max1 = max(array)
   249     14.6 MiB      0.0 MiB       min1 = min(array)
   250     14.6 MiB      0.0 MiB       print(f'Максимальное число в массиве: {max1}')
   251     14.6 MiB      0.0 MiB       print(f'Минимальное число в массиве: {min1}')
   252     14.6 MiB      0.0 MiB       a = array.index(min1)
   253     14.6 MiB      0.0 MiB       b = array.index(max1)
   254     14.6 MiB      0.0 MiB       array.remove(min1)
   255     14.6 MiB      0.0 MiB       array.remove(max1)
   256     14.6 MiB      0.0 MiB       array.insert(a, max1)
   257     14.6 MiB      0.0 MiB       array.insert(b, min1)
   258     15.5 MiB      0.8 MiB       return (f"Новый массив: {array}")

"""
