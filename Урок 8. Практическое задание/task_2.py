"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

# Решил использовать инструменты ООП, мне кажется для данной задачи это наиболее наглядно
# 1) Вычислить частоту использований символов в строке
# 2) Реализовать построение дерева на основании частоты использований символов
# 3) На основании дерева закодировать строку

from collections import Counter, deque


class Node:

    """
    узел дерева
    weight - вес (сумма частот использований символов во всех входящих узлах
    left - левый узел дерева
    right - правый узел дерева
    """

    def __init__(self, weight=None, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node[{self.left}&{self.right}={self.weight}]"


def make_haffman_tree(deque_string):
    """
    формируем дерево на основании очереди
    :param deque_string: очередь кортежей (частоты символов) для формирования дерева
    :return: корневой узел дерева
    """
    while len(deque_string) > 1:
        print(deque_string)  # для наглядности процесса формирования дерева
        # формируем очередной узел из двух левых элементов очереди и удаляем эти два элемента
        weight = deque_string[0][1] + deque_string[1][1]
        node = Node(weight=weight, left=deque_string.popleft()[0], right=deque_string.popleft()[0])
        # вставляем новый элемент в отсортированную очередь
        for i, item in enumerate(deque_string):
            if weight > item[1]:
                continue
            deque_string.insert(i, (node, weight))
            break
        else:
            deque_string.append((node, weight))

    return deque_string[0][0]


def haffman_code(tree, path=''):
    """
    рекурсивная функция кодирования на основании дерева
    таблицу кодировки записываем в глобальную переменную CODE_TABLE
    """
    if not isinstance(tree, Node):
        CODE_TABLE[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


def main():
    """
    основной код
    """
    string = 'beep boop beer!'
    print(f'Строка для кодирования: {string}')
    # 1) Вычислить частоту использований символов в строке
    counter_string = Counter(string)
    print(counter_string)
    # 2) Реализовать построение дерева на основании частоты использований символов
    deque_string = deque(sorted(counter_string.items(), key=lambda item: item[1]))
    node_0 = make_haffman_tree(deque_string)
    # 3) На основании дерева закодировать строку
    haffman_code(node_0)
    print("Таблица кодирования:")
    print(CODE_TABLE)
    print("Закодированная строка:")
    for i in string:
        print(CODE_TABLE[i], end=' ')


# Таблица кодировки символов
CODE_TABLE = dict()

main()

# Результат выполнения программы:
# Строка для кодирования: beep boop beer!
# Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
# deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
# deque([(Node[r&!=2], 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
# deque([(' ', 2), ('o', 2), ('b', 3), (Node[Node[r&!=2]&p=4], 4), ('e', 4)])
# deque([('b', 3), (Node[ &o=4], 4), (Node[Node[r&!=2]&p=4], 4), ('e', 4)])
# deque([(Node[Node[r&!=2]&p=4], 4), ('e', 4), (Node[b&Node[ &o=4]=7], 7)])
# deque([(Node[b&Node[ &o=4]=7], 7), (Node[Node[Node[r&!=2]&p=4]&e=8], 8)])
# Таблица кодирования:
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
# Закодированная строка:
# 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
