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


def huffman_tree(s):
    """'
    Построение дерева для кодирования по алгоритму Хаффмана
    """
    # Подсчет частоты значений
    count_s = Counter(s)
    # Сортировка частот в порядке неубывания
    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))
    # Создание двоичного дерева
    while len(sorted_s) > 1:
        weight = sorted_s[0][1] + sorted_s[1][1]
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])
        # Перемещение узлов и веса на нужное место в список
        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))
    return sorted_s[0][0]


code_table = dict()


def huffman_code(tree, path=''):
    """
    Составление таблицы кодирования по дереву
    """
    if not isinstance(tree, MyNode):
        code_table[tree] = path
    else:
        huffman_code(tree.left, path=f'{path}0')
        huffman_code(tree.right, path=f'{path}1')


S = input('Введите строку для кодировки: ')

# Формирование таблицы кодирования
huffman_code(huffman_tree(S))
# Вывод кода
for i in S:
    print(code_table[i], end=' ')

print()
