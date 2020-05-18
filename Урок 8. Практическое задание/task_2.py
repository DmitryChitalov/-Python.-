"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

import collections


class HuffmanTree:
    def __init__(self, value, left=None, right=None, letter=None):
        self.value = value
        self.left = left
        self.right = right
        self.letter = letter

    def __repr__(self):
        return f'(value = {self.value}, letter = {self.letter}, left = {self.left}, right = {self.right})'


def get_value(hf):
    return hf.value


def before_tree_create(sheet1, sheet2):
    tree = HuffmanTree(sheet1.value + sheet2.value, left=sheet1, right=sheet2, letter=None)
    return tree


def create_leaves(word):
    leaves_list = []
    for value in word:
        letter = HuffmanTree(word[value], letter=value)
        leaves_list.append(letter)
    leaves_list.sort(key=get_value)
    return leaves_list


def set_tree(leaves_list, tree):
    for index, sheet in enumerate(leaves_list):
        if sheet.value == tree.value:
            leaves_list.insert(index, tree)
            return leaves_list
        elif sheet.value < tree.value and index == len(leaves_list) - 1:
            leaves_list.append(tree)
            return leaves_list
        elif sheet.value < tree.value and leaves_list[index + 1].value > tree.value:
            leaves_list.insert(index + 1, tree)
            return leaves_list


def tree_create(leaves):
    while len(leaves) == 2:
        tree = before_tree_create(leaves[0], leaves[1])
        return tree
    else:
        tree = HuffmanTree(leaves[0].value + leaves[1].value, left=leaves.pop(0), right=leaves.pop(0), letter=None)
        set_tree(leaves, tree)
        return tree_create(leaves)


def find_letter_in_tree(tree, find_letter, stack):
    if tree.letter == None:
        if find_letter_in_tree(tree.left, find_letter, stack) != None:
            stack.appendleft(0)
            return stack
        elif find_letter_in_tree(tree.right, find_letter, stack) != None:
            stack.appendleft(1)
            return stack
        else:
            return None
    else:
        if find_letter == tree.letter:
            return True
        else:
            return None


def convert_deque_to_str(deque):
    con_string = ''
    for i in deque:
        con_string += str(i)
    return con_string


def create_encod_table(word, tree):
    encod_table = {}
    for i in word:
        if i not in encod_table:
            stack = collections.deque([])
            encod_table[i] = convert_deque_to_str(find_letter_in_tree(tree, i, stack))
    return encod_table


def Huffman_encod(word):
    word_collections = collections.Counter(word)
    leaves = create_leaves(word_collections)
    tree = tree_create(leaves)
    encod_table = create_encod_table(word, tree)
    coding_word = Huffman_cod(word, encod_table)
    return coding_word, encod_table


def Huffman_cod(word, encod_table):
    coding_word = ''
    for i in word:
        coding_word += encod_table[i]
        coding_word += ' '
    return coding_word


while (1):
    word = input('Введите текст для кодировки: ')
    if word == '':
        print('Строка пуста, попробуйте еще раз!')
    else:
        coding_word, encod_table = Huffman_encod(word)
        print(
            f'Результат кодировки: \n{coding_word}\nТаблица кодировки '
            f'= {encod_table},\n')
        break
