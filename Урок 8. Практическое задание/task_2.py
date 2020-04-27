"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""


import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, seq=''):
        self.left.walk(code, seq + '0')
        self.right.walk(code, seq + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, seq):
        code[self.char] = seq or '0'


def huffman_code(string):
    count = len(string)
    heap = []
    for el, freq in Counter(string).items():
        heap.append((freq, count, Leaf(el)))
        count += 1
    heapq.heapify(heap)
    while len(heap) > 1:
        freq_left, count_left, left = heapq.heappop(heap)
        freq_right, count_right, right = heapq.heappop(heap)
        heapq.heappush(heap, ((freq_left + freq_left), count, Node(left, right)))
        count += 1
    code = {}
    if heap:
        [(freq, count, root)] = heap
        root.walk(code)
    return code


def huffman_encode(string):
    code = huffman_code(string)
    return ' '.join([code[ch] for ch in string])


input_string = input('Enter a string to encode - ')
code_encode = {}
encode_string = huffman_encode(input_string)
print(f'Encrypted string:\n{encode_string}')
