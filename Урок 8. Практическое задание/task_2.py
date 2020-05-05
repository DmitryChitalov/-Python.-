"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter, deque

class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def haffman_tree(s):
    """
    Функция для построения бинарного дерева.
    :param s: строка
    :return:
    """
    count_s = Counter(s)  # выделить частоты с которыми встречаются символы в строке
    # и преобразовать их к отсортированной очереди deque, от наименьшей частоты к большей
    sorted_s = deque(sorted(count_s.items(), key=lambda itm: itm[1]))

    while len(sorted_s) > 1:

        weight = sorted_s[0][1] + sorted_s[1][1]  # сумма частот "листьев" для узла
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])
        # создаётся экземпляр класса, который хранит "листья" дерева,
        # соответствующий элементы извлекаются из очереди

        for num, itm in enumerate(sorted_s):
            # последовательно берётся каждый элемент очереди и строится дерево,
            # состоящее из экземпляров класса MyNode и накопленных частот
            if weight > itm[1]:
                continue
            else:
                sorted_s.insert(num, (node, weight))
                break
        else:
            sorted_s.append((node, weight))

    return sorted_s[0][0]


def haffman_code(tree, path=''):
    """
    Функция для получения пути в бинарном дереве к каждому элементу.
    :param tree: бинарное дерево
    :param path: путь к текущему узлу дерева
    :return:
    """
    if not isinstance(tree, MyNode):
        # если элемент дерева не является экземпляром класса MyNode,
        # то рекурсивные вызовы прекращаются и фиксируется путь к текущему элементу
        code_table[tree] = path

    else:
        # если элемент в очереди всё ещё является экземпляром класса MyNode,
        # рекурсивно вызвать функцию haffman_code и пройти по левой и правой ветке
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


code_table = dict()  # таблица кодов
USER_ENTER = input('Введите строку: ')

haffman_code(haffman_tree(USER_ENTER))

for i in USER_ENTER:
    # вывод кодов элементов через пробел
    print(code_table[i], end=' ')
