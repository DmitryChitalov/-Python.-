"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit

print('Исходное число 2857463584372898347928347923847918273645918273647547563875\n')


def func(count=1, word='', div=10, number=2857463584372898347928347923847918273645918273647547563875):
    if count != 0:
        return func(number // div, word + str(int((number % div) // (div / 10))),
                    div * 10, number)
    return f'Перевернутое число : {word}'


print(func())
print('Время выполнения задачи рекурсией с вычислением числа математическими операциями')
print(timeit.timeit("func()", setup="from __main__ import func", number=100000))


def func_for():
    word = ''
    COUNT = 1
    DIV = 10
    RESULT = 1
    NUMBER = 2857463584372898347928347923847918273645918273647547563875
    while COUNT != 0:
        COUNT = NUMBER // DIV
        RESULT = int((NUMBER % DIV) // (DIV / 10))
        word = f'{word}{str(RESULT)}'
        DIV *= 10

    return f'Перевернутое число : {word}'


print(func_for())
print('Время выполнения задачи циклом с вычислением числа математическими операциями')
print(timeit.timeit("func_for()", setup="from __main__ import func_for", number=100000))

NUMBER = 2857463584372898347928347923847918273645918273647547563875
NUMBER = str(NUMBER)
COUNT_OF = len(NUMBER) - 1
WORD = ''


def func(count=COUNT_OF, word='', number=NUMBER):
    word += number[count]
    if count != 0:
        return func(count - 1, word, number)
    return f'Перевернутое число : {word}'


print(func())
print('Время выполнения задачи рекурсией с вычислением числа конкатенацией')
print(timeit.timeit("func()", setup="from __main__ import func", number=100000))


def func_for():
    word = ''
    NUMBER = 2857463584372898347928347923847918273645918273647547563875
    NUMBER = str(NUMBER)
    for i in range(len(NUMBER), 0, -1):
        word = word + NUMBER[i - 1]
    word = int(word)
    return f'Перевернутое число : {word}'


print(func_for())
print('Время выполнения задачи циклом с вычислением числа конкатенацией')
print(timeit.timeit("func_for()", setup="from __main__ import func_for", number=100000))

print('Для решения задачи по перестановки цифр в числе, гораздо эффективнее представить число в виде строки, скорость\n'
      'решения возрастает в несколько раз. В решении данных задач использовать цикл предпочтительнее , т.к. \n'
      'немого быстрее. ')
