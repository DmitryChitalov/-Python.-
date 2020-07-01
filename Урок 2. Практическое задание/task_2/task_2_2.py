"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


#  Solution from teacher

def recur_method(numb, even=0, odd=0):
    # all digits are extracted
    if numb == 0:
        return even, odd
    else:
        # get the following digit
        cur_n = numb % 10
        # the number becomes shorter
        numb = numb // 10
        # check is this digit odd or even?
        if cur_n % 2 ==0:
            even += 1
            return recur_method(numb, even, odd)
        else:
            odd +=1
            return recur_method(numb, even, odd)
try:
    NUMB = int(input("Enter natural number: "))
    print(f"Number odd and eve digits in this natural number is: {recur_method(NUMB)}")
except ValueError:
    print("You entered a wrong value. Try again")