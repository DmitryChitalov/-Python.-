
from collections import defaultdict, Counter

class Tree():
    min_distance = 5

    # Задает расстояние между элементами дерева при выводе
    @classmethod
    def distance_change(cls, new_distance: int):
        cls.min_distance = new_distance

    # Генерирует индекс для нового объекта
    # Предполагется его уникальность
    # Однако в данном методе возможны повторения
    @staticmethod
    def __generate_number(string):
        number = 0
        for el in string:
            number += ord(el)

        return number
    # Создает строку для вывода на экран
    # В соответствии с глубиной строки
    @staticmethod
    def __getstr(self, level, full=False):
        if level == 1:
            result = '*'
            if self is not None:
                if self.value is not None:
                    if full:
                        result = self.value
                    else:
                        result = self.value['value']

            return str(result) + ' '*Tree.min_distance
        else:
            if self is not None:
                left = Tree.__getstr(self.left, level - 1, full)
                right = Tree.__getstr(self.right, level - 1, full)
            else:
                left = Tree.__getstr(None, level - 1, full)
                right = Tree.__getstr(None, level - 1, full)

            return left + right

    def __init__(self, left=None, right=None, value=None):

        self.left = left
        self.right = right
        self.value = value
        self.parent = None

    # Выводит значение данного элемента
    def __str__(self):

        return f'{self.value["value"]}' if self.value is not None else 'None'

    # Добавляет новый объект в дерево
    def append(self, obj, left=None, right=None):

        index = Tree.__generate_number(str(obj)) # Генерируем индекс
        data = defaultdict() # Создаем элемент объекта
        data['index'] = index
        data['value'] = obj
        if self.value is None: # Если ничего не записано то добавляем в данную ветку дерева
            self.value = data
            self.left = left
            self.right = right
        elif self.value['index'] > index: # Если индекс объекта меньше то идем в левую ветку
            if self.left is None: # Если объект отсутствует , то производим запись
                self.left = Tree(value=data, left = left, right = right)
                self.left.parent = self
            else:
                del data
                self.left.append(obj) # Рекурсивно спускаемся на уровень ниже
        elif self.value['index'] < index: # Если индекс объекта больше то идем в правую ветку
            if self.right is None: # Если объект отсутствует , то производим запись
                self.right = Tree(value=data, left = left, right = right)
                self.right.parent = self
            else:
                del data
                self.right.append(obj) # Рекурсивно спускаемся на уровень ниже
        elif self.value['value'] != obj: # если индексы совпадают, но элементы разные то идем влево
            child = self.left # Сохраняем все данные на левой ветке
            if child is not None: # Если данные не нулевые
                child.level += 1 # Увеличиваем глубину исходной вестки на 1
            self.left = Tree(left= child, value=data)
            # Создаем новую ветку и в левую ветку добавляем сохраняем ветку

    # Находит объект в дереве
    def find(self, obj):

        index = Tree.__generate_number(str(obj)) # Вычисляем индекс объекта
        tmp = self
        if self.value is not None:
            while True:

                if tmp.value['index'] == index: # Если индексы равны
                    if tmp.value['value'] == obj: # Значения равны то объект найден
                        return tmp
                    else: # Идем влево
                        tmp = tmp.left
                elif tmp.value['index'] > index: # Идем влево
                    tmp = tmp.left
                else:
                    tmp = tmp.right # Идем вправо

                if tmp is None: # Если дошли до конца и ничего не нашли
                    return None

    # Удаляет объект в дереве
    def remove(self, obj):

        if self is not None:
            index = Tree.__generate_number(str(obj)) # Вычисляем индекс объекта
            if self.value['index'] == index:
                if self.value['value'] == obj: # Если объект найден
                    if self.right is None and self.left is None:  # Если у него нету второстепенных веток
                        if self.parent.value['index'] <= index: # Если пришли справа
                            self.parent.right = None  # удаляем объект
                        else: # Если пришли слева
                            self.parent.left = None

                    else:
                        # Переносим все элементы справа
                        # Чтобы сохранить порядок сохранения
                        tmp = self
                        while tmp.right is not None: # Пока не дойдем до конца
                            tmp.value = tmp.right.value
                            tmp = tmp.right

                        if tmp.left is None: # Если слева нету веток
                            tmp.remove(tmp.value['value']) # Удаляем последний элемент
                            # Рекурсии не будет так это и есть искомый объект
                        else:
                            tmp.parent.right = tmp.left # Присваиваем всю левую ветку с иерархией

                elif self.left is not None: # Если индексы равны но объекты разные
                    self.left.remove(obj) # Идем влево

            elif self.value['index'] > index and self.left is not None: # Если индекс меньше исходного то идем влево если объект существует
                self.left.remove(obj)
            elif self.value['index'] < index and self.right is not None: # Если индекс больше исходного то идем вправо если объект существует
                self.right.remove(obj)

            # В противном случае объекта не было изначально

    # Выводит дерево на экран
    def show_tree(self, data_only=True):

        cur_level = 1
        while True:
            test = ('*' + ' ' * Tree.min_distance) * (pow(2, cur_level-1))
            if data_only: # выводит только значение value
                line = Tree.__getstr(self, cur_level)

            else: # Выводит всю информацию в ячейке
                line = Tree.__getstr(self, cur_level, True)

            if line == test:
                break
            else:
                cur_level += 1
                print(line)

class Haffman(Tree):

    # Сортирует исходный Counter
    @staticmethod
    def __frequency_sort(data):
        result = []
        start = True
        for el in data: # Для каждого элемента
            if start:
                result.append([el, data[el]]) # Добавляем элемент и его частоту
                start = False

            else: # Если не начало цикла
                i = 0
                while result[i][1] < data[el]: # Пока частота в конечном массиве меньше чем у элемента
                    i += 1 # Идем вправо
                    if i >= len(result): # Если дошли до конца
                        break
                result.insert(i, [el, data[el]]) # Вставляем элемент по найденному индексу

        return result

    # Задает закодированную строку при помощи таблицы соответствия
    @staticmethod
    def __get_code_string(string, table):

        coded_str = ''
        for s in string: # Кодируем каждый символ в исходной строке
            coded_str += table[s] + ' ' # Разделяем код пробелом

        return coded_str

    # Обновляет кодровку символов в таблице
    @staticmethod
    def __update_code(table, obj, number: str):

        if table.get(obj.value['value']) is not None: # Если элемент есть в таблице соответствия
            table[obj.value['value']] = number + table[obj.value['value']] # Добавляем 0 или 1 слева к исходному коду

        if obj.left is not None: # Если слева есть ветки
            Haffman.__update_code(table, obj.left, number) # Рекурсивно добавляем число к данным слева

        if obj.right is not None: # Аналогично справа
            Haffman.__update_code(table, obj.right, number)

    def __init__(self, left=None, right=None, value=None, code_table=None):
        super().__init__(left=left, right=right, value=value)
        self.code_table = code_table
        self.primary_data = None
        self.sorted_data = None

    # Кодирует исходную строку
    def encode(self, string: str, use_code_table=False):

        if use_code_table: # Если использовать таблицу
            if self.code_table is None: # Если её нету
                return 'No code table'
            return Haffman.__get_code_string(string, self.code_table) # Возвращаем закодированную строку

        data = Counter(string) # Преобразуем исходную строку в Counter
        self.primary_data = data # Cохраняем полученную информацию ( Данная переменная не является обязательной и служит только на наглядности вывода )
        table = {el: '' for el in data} # Генерируем таблицу соответствия в соответствии с полученными данными
        data = Haffman.__frequency_sort(data) # Сортируем Counter
        self.sorted_data = data.copy() # Сохраняем результат ( Данная переменная не является обязательной и служит только на наглядности вывода )

        while len(data) > 1:
            tmp_l = data.pop(0) # Извлекаем левую ветку. Длина уменьшилась на 1
            tmp_r = data.pop(0) # Извлекаем правую ветку. Длина уменьшилась на 1
            tree = Haffman() # Создаем дерево

            if isinstance(tmp_l[0], Haffman): # Если левая ветка - объект класса Haffman
                left = tmp_l[0]
            else: # В противном случае создаем объект класса Haffman
                left = Haffman()
                left.append(obj=tmp_l[0])

            # Аналогично для правой ветки
            if isinstance(tmp_r[0], Haffman):
                right = tmp_r[0]
            else:
                right = Haffman()
                right.append(obj=tmp_r[0])

            # Находим частоту и значение ветки родителя
            parent = tmp_l[1] + tmp_r[1]
            tree.append(obj = parent, left =left, right = right ) # Создаем родительскую ветку

            # Обновляем таблицу для левой и правой ветки соответственно
            Haffman.__update_code(table, left, '0')
            Haffman.__update_code(table, right, '1')

            # Проводим дополнительную сортировку
            i = 0
            if len(data) > 0:
                while parent > data[i][1]:
                    i += 1
                    if i >= len(data):
                        break
            data.insert(i, [tree, parent])

        # В конце останется только один элемент [[ Haffman , frequency ]]
        # Сохраняем полученные данные в исходном объекте
        self.append(obj = data[0][0].value['value'], left=data[0][0].left, right=data[0][0].right)
        # Глубина = максимальная длина кодировки + 1 верхний элемент
        self.code_table = table # Сохраняем полученную таблицу

        del data, tree, left, right
        return Haffman.__get_code_string(string, table) # Возвращаем кодированную строку
    # Декодирует строку если есть таблица
    def decode(self, code_str):

        if self.code_table is not None: # Если есть таблица соответствия
            string = ''
            code = code_str.split(' ') # Массив закодированных символов
            for el in code: # Декодируем каждый элемент
                for key, value in self.code_table.items():
                    if value == el:
                        string += key
                        break
            return string
        else:
            return 'No code table'

if __name__ == '__main__' :

    test = Tree()

    tree = Tree()
    tree.append('test')
    haffman = Haffman()
    haffman.append(5)

    test.append(12)
    test.append('string')
    test.append(12.34)
    test.append(tree)
    test.append({'dict': 'Some data'})
    test.append(haffman)
    test.append(haffman.encode('hello world!'))
    test.show_tree(data_only=True)
    print()
    test.show_tree(data_only=False)
    find_obj = test.find(tree)
    print()
    print(find_obj)
    test.remove('string')
    print()
    test.show_tree(data_only=True)
    print()
    test.remove(12)
    test.show_tree(data_only=True)
    test.remove(haffman)
    print()
    test.show_tree(data_only=True)




