"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter, deque


def haffman_tree(s):

    frequenc = Counter(s)
    sorted_elements = deque(sorted(frequenc.items(), key=lambda item: item[1]))
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            knot = sorted_elements[0][1] + sorted_elements[1][1]
            # Словарь из 2 крайних левых элементов, попутно вырезаем их
            # из "sorted_elements" (из очереди).
            # comb - объединенный элемент
            '''
            {0: 'r', 1: '!'}
            {0: {0: 'r', 1: '!'}, 1: 'p'}
            {0: ' ', 1: 'o'}
            {0: 'b', 1: {0: ' ', 1: 'o'}}
            {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
            {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
            '''
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}

            for i, _count in enumerate(sorted_elements):
                if knot > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, knot))
                    break
            else:
                sorted_elements.append((comb, knot))
    else:
        knot = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, knot))
    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "глокая куздра будланула бокра"

haffman_code(haffman_tree(s))

print(*[code_table[x] for x in s])