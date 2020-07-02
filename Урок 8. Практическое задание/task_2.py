"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import deque, Counter


def haffman_code(s):
    c = Counter(s)
    d = deque(sorted(c.items(), key=lambda el: el[1]))
    if len(d) != 1:
        while len(d) > 1:
            weight = d[0][1] + d[1][1]
            two = {
                0: d.popleft()[0],
                1: d.popleft()[0]
            }

            for i in range(len(d)):
                if d[i][1] >= weight:
                    d.insert(i, (two, weight))
                    break
            else:
                d.append((two, weight))
    else:
        weight = d[0][1]
        two = {
            0: d.popleft()[0],
            1: None
        }
        d.append((two, weight))
    return d[0][0]


def rec_haf(tree, path=''):
    if not isinstance(tree, dict):
        res[tree] = path
    else:
        rec_haf(tree[0], path=f'{path}0')
        rec_haf(tree[1], path=f'{path}1')


s = 'Удивительно, но работает!'
# s = "beep boop beer!"

res = dict()
tree = haffman_code(s)
rec_haf(tree)
for el in s:
    print(res[el], end=' ')
print()
for key, items in res.items():
    print(f'{key} - {items}')

# Также писал сам, но пришлось довольно часто заглядывать, в итоге не сильно отошел от примера,
# но разобрался со всем, даже на листочке самостоятельно расписал как
# дерево строится для лучшего понимания
