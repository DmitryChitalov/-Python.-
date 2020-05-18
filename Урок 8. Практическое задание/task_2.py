"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque


class Node:  # класс для ветвей дерева - внутренних узлов
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(string):
    """Ф-ия для построенния бинарного дерева"""
    count_str = Counter(string)  # Подсчет частот встречаемости символа
    sorted_str = deque(sorted(count_str.items(), key=lambda x: x[1]))
    while len(sorted_str) > 1:  # дерево будет строиться, пока будет оставаться, хотя бы 2 элемента
        weight = sorted_str[0][1] + sorted_str[1][1]
        node = Node(left=sorted_str.popleft()[0], right=sorted_str.popleft()[0])

        for j, item in enumerate(sorted_str):
            if weight > item[1]:
                continue
            else:
                sorted_str.insert(j, (node, weight))
                break
        else:
            sorted_str.append((node, weight))

    return sorted_str[0][0]


code_table = dict()  # словарь для хранения пары "символ


def huffman_code(tree, path=''):
    """Ф-ия для кодирования элементов дерева"""
    if not isinstance(tree, Node):
        code_table[tree] = path
    else:
        huffman_code(tree.left, path=f'{path}0')
        huffman_code(tree.right, path=f'{path}1')


s = "beep boop beer!"
huffman_code(huffman_tree(s))

for i in s:
    print(code_table[i], end=' ')

print()
