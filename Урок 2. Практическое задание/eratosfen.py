"""
Программная реализация алгоритма «Решето Эратосфена»
"""


def recursion_check_number(rc_list, r_index, r_number) -> list:
    """ Рекурсивный перебор списка вместо цикла for """
    if r_index >= len(rc_list):
        return rc_list

    if (rc_list[r_index] > r_number) and (rc_list[r_index] % r_number) == 0:
        rc_list[r_index] = 0
    return recursion_check_number(rc_list, r_index + 1, r_number)


def recursion_list(rl_list, r_position, r_n) -> list:
    """ Рекурсивный перебор списка вместо цикла while """
    if rl_list[r_position] ** 2 > r_n:
        return rl_list

    if rl_list[r_position] != 0:
        rl_list = recursion_check_number(
            rl_list, r_position, rl_list[r_position])
        return recursion_list(rl_list, r_position + 1, r_n)
    return recursion_list(rl_list, r_position + 1, r_n)


def eratosfen() -> None:
    """ Решето Эратосфена """
    try:
        n_value = abs(
            int(input('Введите верхнюю границу массива простых чисел: ').strip())
        )
        start_list = []
        simple_list = []
        for i in range(2, n_value + 1):
            start_list.append(i)

        print('Исходный массив:\n', start_list)

        start_list = recursion_list(start_list, 0, n_value)

        for item in start_list:
            if item != 0:
                simple_list.append(item)
        del start_list

        print('Конечный массив:\n', simple_list)

    except ValueError:
        print('Некорректный ввод. Выходим.')


if __name__ == "__main__":
    eratosfen()
