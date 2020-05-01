"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter


class TreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Haffman:
    _codes = dict()
    _tree = TreeNode(None, None)

    # Разбор входной строки и назначение кода каждому символу
    def parse(self, string):
        # Подсчитаем вхождение каждого элемента в строке
        counter = Counter(string)
        elements = sorted(counter.items(), key=lambda item: item[1])

        if len(elements) > 1:
            while len(elements) > 1:
                weight = elements[0][1] + elements[1][1]
                node = TreeNode(elements.pop(0)[0], elements.pop(0)[0])

                # Ищем, куда вставить новый элемент
                for i, item in enumerate(elements):
                    if weight > item[1]:
                        continue
                    else:
                        elements.insert(i, (node, weight))
                        break
                else:
                    elements.append((node, weight))
        # Разбираем коды
        self._tree = elements[0][0]
        self.haffman_code(self._tree)

    @classmethod
    # Рекурсивно обходим дерево и присваиваем коды каждому символу
    def haffman_code(cls, tree, path=''):
        if not isinstance(tree, TreeNode):
            cls._codes[tree] = path
        else:
            cls.haffman_code(tree.left, path=f'{path}0')
            cls.haffman_code(tree.right, path=f'{path}1')

    # Декодирует на основе текущего словаря
    def decode(self, string):
        result = ''
        cur_elem = self._tree
        for i in string:
            # Выбираем, по какой ветке пойти
            if i == '0':
                cur_elem = cur_elem.left
            else:
                cur_elem = cur_elem.right
            # Проверяем, что достигли листа
            if not isinstance(cur_elem, TreeNode):
                result += cur_elem
                cur_elem = self._tree
        return result

    # Кодирует строку
    def encode(self, string):
        result = ''
        try:
            for i in string:
                result += self._codes[i] + ' '
        except KeyError:
            print(f'Не удалось закодировать строку, отсутствует код для "{i}"')
            result = ''
        return result


if __name__ == '__main__':
    haffman = Haffman()
    haffman.parse('beep boop beer!')
    print(haffman.encode('beer bro porez'))
    print(haffman.encode('beer bro pore'))
    res = haffman.encode('beep boop beer!')
    print(res)
    # Также можно декодировать зашифрованную строку
    code = res.replace(' ', '')
    res = haffman.decode(code)
    print(res)

