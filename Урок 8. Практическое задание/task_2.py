"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""


from collections import Counter, deque


class HNode:
    """ Класс узла двоичного дерева """

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        """ Возврат левой и правой частей """
        return self.left, self.right


def frequency_matrix(user_str: str) -> deque:
    """ Создание частотной матрицы """
    f_matrix = Counter(user_str).items()
    f_matrix = sorted(f_matrix, key=lambda x: x[1])
    return deque(f_matrix)


def huffman_tree(f_matrix: deque) -> deque:
    """ Создание бинарного дерева """
    while len(f_matrix) > 1:

        weight = f_matrix[0][1] + f_matrix[1][1]
        node = HNode(left=f_matrix.popleft()[0], right=f_matrix.popleft()[0])

        for i, item in enumerate(f_matrix):
            if weight > item[1]:
                continue
            else:
                f_matrix.insert(i, (node, weight))
                break
        else:
            f_matrix.append((node, weight))

    return f_matrix[0][0]


def codetable(node: HNode, code='') -> dict:
    """ Построение кодовой таблицы """
    if isinstance(node, str):
        return {
            node: code
        }

    result_dict = {}
    left, right = node.children()
    result_dict.update(codetable(left, code + "0"))
    result_dict.update(codetable(right, code + "1"))
    return result_dict


def decode(user_str: str, codetable_d: dict) -> str:
    """ Кодирование строки в соответствии с кодовой таблицей"""
    result_str = ''
    for letter in user_str:
        result_str += codetable_d.get(letter) + ' '
    return result_str[:-1]


if __name__ == "__main__":

    TEST_STRING = "beep boop beer!"
    TEST_RESULT = '00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001'
    CODETABLE_DICT = codetable(huffman_tree(frequency_matrix(TEST_STRING)))
    DECODED_STRING = decode(TEST_STRING, CODETABLE_DICT)
    print(DECODED_STRING)
    print('Результат корректен?: ', TEST_RESULT == DECODED_STRING)
