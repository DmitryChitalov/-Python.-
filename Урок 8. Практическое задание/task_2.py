"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    """класс для ветвей дерева - внутренних узлов; у них есть потомки"""
    def walk(self, code, acc):
        """чтобы обойти дерево нам нужно"""
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):
    """класс для листьев дерева, у него нет потомков, но есть значение символа"""
    def walk(self, code, acc):
        """чтобы обойти лист делать ничего не нужно"""
        code[self.char] = acc or "0"


def huffman_encode(s):
    """функция кодирования строки в коды Хаффмана"""
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")

    encoded = "".join(code[ch] for ch in s)
    return code, encoded  # возвращаем словарь символов и соответствующих им кодов и результ


def huffman_decode(encoded, code):
    """функция декодирования исходной строки по кодам Хаффмана"""
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)  # вернем значение раскодированной строки


def main():
    """main"""
    s = input()
    code, encoded = huffman_encode(s)
    print_code(code, s, encoded)


def test():
    """тест для проверки алгоритма"""
    for s in ["beep boop beer!", "python python", "a", "qqqqq"]:
        code, encoded = huffman_encode(s)
        print_code(code, s, encoded)
        # раскодируем строку и сравним ее с исходной строкой
        assert huffman_decode(encoded, code) == s


def print_code(code, original, encoded):
    """Вывод результатов на экран"""
    encoded_visual = "".join(
        code[ch] + " " for ch in original)

    print("{} ({}) -> {} ({})".format(original, len(original), encoded_visual, len(encoded) // 8 + 1))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код


# запускаем
# main()
test()
