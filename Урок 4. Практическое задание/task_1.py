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
# импортируем модули для анализа
import timeit
import cProfile

# возьмем задания из второго урока task_2
# Метод 1, цикл


def task_cycle():
    # вместо ввода пользователя задаем вручную исходные данные
    user_number = 34560

    # вводим счетчики для четных и нечетных чисел
    even_number = 0
    odd_number = 0

    # натуральное число больше 0, проверяем
    if user_number > 0:
        # введем переменную, чтобы использовать для вычислений
        # исходное число сохраним для вывода результата
        oper_number = user_number
        # теперь можно приступить к циклу: пока число больше 0
        while oper_number > 0:
            # если число нацело делится на 2, значит оно четное,
            # играет роль последняя цифра в числе, иначе нечетное (цифра)
            if oper_number % 2 == 0:
                even_number += 1
            else:
                odd_number += 1
            # уменьшаем число на десяток
            oper_number = oper_number // 10
        # вывод на экран производить не будем
        # print(f'В числе {USER_NUMBER} всего {len(str(USER_NUMBER))} цифр, '
        #       f'из которых {EVEN_NUMBER} четных и {ODD_NUMBER} нечетных')


# Метод 2, рекурсия


def task_recursion():
    def recursion(number, even_number=0, odd_number=0):
        """
        Функция принимает на входе число и счетчики
        По-умолчанию счетчики равны нулю
        :return: завершение рекурсии, вывод результата
        """
        if number == 0:
            # вывод на экран производить не будем
            # print(f'Количество четных и нечетных цифр в числе равно: ({even_number}, {odd_number})')
            return

        if number % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
        number = number // 10
        recursion(number, even_number, odd_number)

    # вместо ввода пользователя задаем вручную исходные данные
    user_number = 34560

    # вызываем нашу функцию recursion, передавая параметром число
    recursion(user_number)


# выполним анализ времени выполнения обоих решений
print(f'Время выполнения решения циклом: '
      f'{timeit.timeit("task_cycle()", setup="from __main__ import task_cycle")}')
print(f'Время выполнения решения рекурсией: '
      f'{timeit.timeit("task_recursion()", setup="from __main__ import task_recursion")}')


# выполним профилировку каждого куска кода
cProfile.run('task_cycle()')
cProfile.run('task_recursion()')

# Вывод
# Мы видим, что время выполнения задачи циклом меньше, т.е.
# задача выполнена быстрее, чем рекурсией.
# Также, благодаря cProfile мы видим, что узких мест нет.
# В случае с рекурсией, сама функция вызывается 1 раз, в то время как
# сама себя она вызывает 6 раз.
# Таким образом, принимаем решение циклом более оптимальным.
