"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter
import heapq

class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code_dict, path):
        self.left.walk(code_dict, path + "0")
        self.right.walk(code_dict, path + "1")


class Leaf:
    def __init__(self, value):
        self.value = value

    def walk(self, code_dict, path):
        code_dict[self.value] = path
        return path


def Huffman(s):
    lst = []

    for i, item in Counter(s).items():
        lst.append((item, len(lst), Leaf(i)))

    iteration = len(lst)
    heapq.heapify(lst)
    while len(lst) > 1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        heapq.heappush(lst, (first[0] + second[0], iteration, MyNode(first[2], second[2])))
        iteration += 1

    code_dict = {}
    if lst:
        lst[0][2].walk(code_dict, "")
    return code_dict

s = 'beep boop beer!'
print(f'The string: \n{s}')
s = Counter(s)
print(s)
d = Huffman(s)
print(d)
for key, value in d.items():
    print(f'{key}: {value}')

s = 'The quick brown fox jumps over the lazy dog.'
print(f'The string: \n{s}')
s = Counter(s)
print(s)
d = Huffman(s)
print(d)
for key, value in d.items():
    print(f'{key}: {value}')
