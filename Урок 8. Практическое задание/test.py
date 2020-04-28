import heapq
from collections import Counter, namedtuple


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, seq=''):
        self.left.walk(code, seq + '0')
        self.right.walk(code, seq + '1')


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, seq):
        code[self.char] = seq or '0'


def huffman_code(string):
    count = len(string)
    queue = []
    for char, freq in Counter(string).items():
        queue.append((freq, count, Leaf(char)))
        count += 1
    heapq.heapify(queue)
    while len(queue) > 1:
        freq_left, count_left, left = heapq.heappop(queue)
        freq_right, count_right, right = heapq.heappop(queue)
        heapq.heappush(queue, (freq_left + freq_right, count, Node(left, right)))
        count += 1
    code = {}
    if queue:
        [(freq, count, root)] = queue
        root.walk(code)
    return code


def huffman_encode(string):
    code = huffman_code(string)
    return ''.join([code[char] for char in string]), code


def huffman_decode(string, code):
    code_decode = {}
    for key, value in code.items():
        code_decode[value] = key
    output = ''
    el_code = ''
    for i in range(len(string)):
        el_code += string[i]
        if el_code in code_decode:
            output += code_decode[el_code]
            el_code = ''
    return output


def print_code(code):
    if len(code):
        max_len = len(sorted([v for k, v in code.items()], reverse=True)[0])
        print('Dictionary of Encoding:')
        for k, v in code.items():
            print(f'{k} - {str(v).rjust(max_len)}')


user_string = input('Enter a string to encode - ')
encode_string, encode_code = huffman_encode(user_string)
decode_string = huffman_decode(encode_string, encode_code)

print(f'Encrypted string:\n{encode_string}\n')
print(f'Decrypted string:\n{decode_string}\n')
print_code(encode_code)







