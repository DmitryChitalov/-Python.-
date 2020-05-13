"""
Cформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from memory_profiler import profile

# определение
@profile
def recur(number, digit=""):
    """ тут какое-то описсание функции"""
    if number == 0:
        return digit
    else:
        digit = str(number % 10)
        return digit + str(recur(number // 10))

# поехали

@profile
def foo(number):
    USER_NUMBER = number
    NUMBER = ""

    i = CUANTITY = len(str(USER_NUMBER))
    while i > 0:
        Y = USER_NUMBER % 10
        USER_NUMBER = USER_NUMBER // 10
        NUMBER = NUMBER + str(Y)

        i = i - 1
        return NUMBER


print(foo(44588884445321128899878412241254))

print(recur(44588884445321128899878412241254))

print(recur(123456))

print(recur(123))

'''


 28     13.8 MiB     13.8 MiB   @profile
    29                             def foo(number):
    30     13.8 MiB      0.0 MiB       USER_NUMBER = number
    31     13.8 MiB      0.0 MiB       NUMBER = ""
    32                             
    33     13.8 MiB      0.0 MiB       i = CUANTITY = len(str(USER_NUMBER))
    34     13.8 MiB      0.0 MiB       while i > 0:
    35     13.8 MiB      0.0 MiB           Y = USER_NUMBER % 10
    36     13.8 MiB      0.0 MiB           USER_NUMBER = USER_NUMBER // 10
    37     13.8 MiB      0.0 MiB           NUMBER = NUMBER + str(Y)
    38                             
    39     13.8 MiB      0.0 MiB           i = i - 1
    40     13.8 MiB      0.0 MiB           return NUMBER


Line #    Mem usage    Increment   Line Contents
================================================
    24     13.9 MiB     13.9 MiB   @profile
    25                             def recur(number, digit=""):
    26                                 """ тут какое-то описсание функции"""
    27     13.9 MiB      0.0 MiB       if number == 0:
    28     13.9 MiB      0.0 MiB           return digit
    29                                 else:
    30     13.9 MiB      0.0 MiB           digit = str(number % 10)
    31     13.9 MiB      0.0 MiB           return digit + str(recur(number // 10))
    
    
    
    
Вывод: не важно сколько цифр будет в переменной, занимаемая память практически не меняется( у меня 
цифры были вообще одинаковые хоть 3-х значное число хоть самый первый не знаю кто") поэтому только одна
таблица. Как и предполагалось рекурсия чуть больше требует памяти.



'''