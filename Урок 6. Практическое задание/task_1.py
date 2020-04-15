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

"""
За основу взял задачу :
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

На данном примере сравнивал объем памяти выделяемый на цикл,рекурсию
и с использованием ООП.
Использовал модуль pympler для определения памяти конкретной функции или класса.
Результат рекурсии и цикла - идентичен.

Также сравнил решение этой же задачи с помощью ООП.Замеры проводил по тому
же принципу,только с использованием __slots__ или без.
Метод __slots__ существенно экономит память.

Что же касаемо модуля memory_profiler ,то везде в моих примерах
инкремент ,по ходу программы,никак не менялся.Инкремент,как и общее выделение памяти
фиксировался при запуске программы с первой строкой и более не менялся до конца 
работы программы.

Также что еще подчеркнул из работы с памятью:
-Python управляет объектами с помощью подсчета ссылок.
Диспетчер памяти подсчитывает количество ссылок,выделяемое на каждый объект.
-разные типы данных занимают разный объем памяти.К примеру строка занимает больше памяти,
чем целове число и т.д.
-генераторы существенно увеличивают производительность.Особенно это
хорошо видно на больших входных данных.Это связано с тем,что
генератор не создает промежуточные списки,а выдает данные по запросу(работает лениво).
-array и numpy.array занимают меньше памяти,чем списки.

MacOS - Catalina. x64
Python 3.7.4
"""

from pympler import asizeof


def cycle(numbers):
    """
    вариант с использованием цикла
    """
    if numbers > 0:
        even_score = 0
        not_even_score = 0
        count_of_numbers = 0
        for el in str(numbers):
            count_of_numbers += 1
            if int(el) % 2 == 0:
                even_score += 1
            else:
                not_even_score += 1
        return f'Even :({even_score} not even :{not_even_score})'


def even_count(number, even_score, not_even_score):
    """
    вариант c использованием рекурсии
    """
    if int(number) > 0 and int(number) % 2 == 0:
        even_score += 1
        return even_count(number // 10, even_score, not_even_score)
    elif int(number) > 0:
        not_even_score += 1
        return even_count(number // 10, even_score, not_even_score)
    return f'Even :({even_score} not even :{not_even_score})'

# варианты с использованием ООП

class Task:
    """
    без __slots__
    """
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_score = 0
        self.not_even_score = 0
        self.count_of_numbers = 0


    def __call__(self, *args, **kwargs):
        for el in str(self.numbers):
            self.count_of_numbers += 1
            if int(el) % 2 == 0:
                self.even_score += 1
            else:
                self.not_even_score += 1
        return f'Even : {self.even_score} and not even : {self.not_even_score}'


class Task_slots:
    """
    с использованием __slots__
    """
    __slots__ = ('numbers', 'even_score', 'not_even_score', 'count_of_numbers')
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_score = 0
        self.not_even_score = 0
        self.count_of_numbers = 0


    def __call__(self, *args, **kwargs):
        for el in str(self.numbers):
            self.count_of_numbers += 1
            if int(el) % 2 == 0:
                self.even_score += 1
            else:
                self.not_even_score += 1
        return f'Even : {self.even_score} and not even : {self.not_even_score}'

TS = Task_slots(123213) # экземпляр класса с __slots__
T = Task(123213)# экземпляр класса без __slots__


print(f'Общий объем занимаемой памяти функции'
      f'c использованием цикла : {asizeof.asizeof(cycle(123213))}')
print(f'Общий объем занимаемой памяти функции'
      f'с использованием рекурсии: {asizeof.asizeof(even_count(123213, even_score=0, not_even_score=0))}')

print(f'Общая память потребляемая классом БЕЗ '
      f'использованием метода __slots__ : {asizeof.asizeof(T)}')
print(f'Общая память потребляемая классом С '
      f'использованием метода __slots__ : {asizeof.asizeof(TS)}')


"""
Результаты profile :
Line #    Mem usage    Increment   Line Contents
================================================
    53     23.1 MiB     23.1 MiB   @profile
    54                             def cycle(numbers):
    55                                 
    56                                 вариант с использованием цикла
    57                                 
    58     23.1 MiB      0.0 MiB       if numbers > 0:
    59     23.1 MiB      0.0 MiB           even_score = 0
    60     23.1 MiB      0.0 MiB           not_even_score = 0
    61     23.1 MiB      0.0 MiB           count_of_numbers = 0
    62     23.1 MiB      0.0 MiB           for el in str(numbers):
    63     23.1 MiB      0.0 MiB               count_of_numbers += 1
    64     23.1 MiB      0.0 MiB               if int(el) % 2 == 0:
    65     23.1 MiB      0.0 MiB                   even_score += 1
    66                                         else:
    67     23.1 MiB      0.0 MiB                   not_even_score += 1
    68     23.1 MiB      0.0 MiB           return f'Even :({even_score} not even :{not_even_score})'
    
    Line #    Mem usage    Increment   Line Contents
================================================
    70     23.1 MiB     23.1 MiB   @profile
    71                             def even_count(number, even_score, not_even_score):
    72                                 
    73                                 вариант c использованием рекурсии
    74                                 
    75     23.1 MiB      0.0 MiB       if int(number) > 0 and int(number) % 2 == 0:
    76                                     even_score += 1
    77                                     return even_count(number // 10, even_score, not_even_score)
    78     23.1 MiB      0.0 MiB       elif int(number) > 0:
    79                                     not_even_score += 1
    80                                     return even_count(number // 10, even_score, not_even_score)
    81     23.1 MiB      0.0 MiB       return f'Even :({even_score} not even :{not_even_score})'
    
    
"""