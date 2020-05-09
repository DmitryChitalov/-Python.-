"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter


USER_STRING = input("Введите строку чтобы закодировать: ")
USER_STRING_COUNTER = Counter(USER_STRING)
FINAL_DICT = USER_STRING_COUNTER.most_common()[::-1]
ENC_STRING = []


def my_tree(my_list):
    """Составляем дерево в виде кортежа"""
    if len(my_list) == 1:
        return my_list
    buffer = (my_list[0][0], my_list[1][0]), my_list[0][1] + my_list[1][1]
    my_list.pop(1)
    my_list.pop(0)
    if len(my_list) == 0:
        my_list.append(buffer)
    else:
        for i in range(len(my_list)):
            if buffer[1] <= my_list[i][1]:
                my_list.insert(i, buffer)
                break
            if i + 1 == len(my_list):
                my_list.append(buffer)
    my_tree(my_list)


# Убираем лишнюю информацию
my_tree(FINAL_DICT)
USER_TREE = FINAL_DICT[0][0]
print(f"Закодированный список:\n{USER_TREE}")
print("________________________________________")


# Немного переделал функцию из примера
def haffman_code(tree, current_letter, path=''):
    """Теперь эта функция не создает словарь, а дополняет словарь с закодированной строкой
    новой буквой в закодированном виде
    """
    if not isinstance(tree, tuple):
        if tree == current_letter:
            ENC_STRING.append(path)

    else:
        haffman_code(tree[0], current_letter, path=f'{path}0')
        haffman_code(tree[1], current_letter, path=f'{path}1')


for i in USER_STRING:
    haffman_code(USER_TREE, i)

print("Закодированное сообщение: ", " ".join(ENC_STRING))
