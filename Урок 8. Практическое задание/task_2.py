"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter


def get_counter(my_str):
    return Counter(my_str)


def get_min_weight_idx(my_list):
    min_val, min_idx = my_list[0][1], 0
    for idx, val in enumerate(my_list[1:]):
        if val[1] < min_val:
            min_val, min_idx = val[1], idx + 1
    return min_idx


def create_tree(my_list):
    a1 = my_list.pop(get_min_weight_idx(my_list))
    a2 = my_list.pop(get_min_weight_idx(my_list))
    my_list.append(((a2[0], a1[0]) if a1[1] > a2[1] else (a1[0], a2[0]), a2[1] + a1[1]))
    return my_list[0][0] if len(my_list) == 1 else create_tree(my_list)


def create_table_prep(my_tree, tmp_idx=''):
    if isinstance(my_tree, str):
        return my_tree
    return [[tmp_idx+str(idx), create_table_prep(_, tmp_idx+str(idx))] for idx, _ in enumerate(my_tree)]


def create_table(my_tree):
    global table, reverse_table
    if isinstance(my_tree, str):
        return
    if isinstance(my_tree, list) and isinstance(my_tree[1], str):
        table.setdefault(my_tree[1], my_tree[0])
        reverse_table.setdefault(my_tree[0], my_tree[1])
    else:
        for _ in my_tree:
            create_table(_)


def get_code_string(code_table, my_str):
    return ''.join(code_table.get(_) for _ in my_str)


def get_encodes_string(code_table, my_str, start_pos=0, finish_pos=1):
    if finish_pos > len(my_str):
        return ''
    my_code = my_str[start_pos:finish_pos]
    if code_table.get(my_code) is None:
        return get_encodes_string(code_table, my_str, start_pos, finish_pos+1)
    else:
        return code_table.get(my_code) + get_encodes_string(code_table, my_str, finish_pos, finish_pos+1)


my_string = 'отпуск по беременности и родам (проставляете только первый месяц ухода в декрет, в случае если в этом месяце сотрудник ещё работал)'
table = {}
reverse_table = {}

a = get_counter(my_string)
aa = create_tree(a.most_common())
b = create_table_prep(aa)
create_table(b)
coded_str = get_code_string(table, my_string)
encoded_str = get_encodes_string(reverse_table, coded_str)

print('Исходная строка: ', my_string)
print('Counter: ', a)
print('Дерево: ', aa)
print('Предварительная обработка для таблицы: ', b)
print('Таблица соответствия: ', table)
print('Обратная таблица соответствия: ', reverse_table)
print()
print('Исходная строка: ', my_string)
print('Закодированная строка: ', coded_str)
print('Раскодированная строка: ', encoded_str)

"""
Исходная строка:  отпуск по беременности и родам (проставляете только первый месяц ухода в декрет, в случае если в этом месяце сотрудник ещё работал)
Counter:  Counter({' ': 20, 'е': 14, 'о': 11, 'т': 9, 'с': 8, 'р': 7, 'а': 6, 'м': 5, 'в': 5, 'л': 5, 'п': 4, 'у': 4, 'к': 4, 'и': 4, 'д': 4, 'н': 3, 'я': 3, 'б': 2, 'ц': 2, '(': 1, 'ь': 1, 'ы': 1, 'й': 1, 'х': 1, ',': 1, 'ч': 1, 'э': 1, 'щ': 1, 'ё': 1, ')': 1})
Дерево:  (((('а', ('н', 'я')), 'е'), (('р', ((')', 'б'), 'п')), ('с', ('у', 'к')))), (((('и', 'д'), (('ц', ('(', 'ь')), (('ы', 'й'), ('х', ',')))), ('т', ((('ч', 'э'), ('щ', 'ё')), 'м'))), (' ', (('в', 'л'), 'о'))))
Предварительная обработка для таблицы:  [['0', [['00', [['000', [['0000', 'а'], ['0001', [['00010', 'н'], ['00011', 'я']]]]], ['001', 'е']]], ['01', [['010', [['0100', 'р'], ['0101', [['01010', [['010100', ')'], ['010101', 'б']]], ['01011', 'п']]]]], ['011', [['0110', 'с'], ['0111', [['01110', 'у'], ['01111', 'к']]]]]]]]], ['1', [['10', [['100', [['1000', [['10000', 'и'], ['10001', 'д']]], ['1001', [['10010', [['100100', 'ц'], ['100101', [['1001010', '('], ['1001011', 'ь']]]]], ['10011', [['100110', [['1001100', 'ы'], ['1001101', 'й']]], ['100111', [['1001110', 'х'], ['1001111', ',']]]]]]]]], ['101', [['1010', 'т'], ['1011', [['10110', [['101100', [['1011000', 'ч'], ['1011001', 'э']]], ['101101', [['1011010', 'щ'], ['1011011', 'ё']]]]], ['10111', 'м']]]]]]], ['11', [['110', ' '], ['111', [['1110', [['11100', 'в'], ['11101', 'л']]], ['1111', 'о']]]]]]]]
Таблица соответствия:  {'а': '0000', 'н': '00010', 'я': '00011', 'е': '001', 'р': '0100', ')': '010100', 'б': '010101', 'п': '01011', 'с': '0110', 'у': '01110', 'к': '01111', 'и': '10000', 'д': '10001', 'ц': '100100', '(': '1001010', 'ь': '1001011', 'ы': '1001100', 'й': '1001101', 'х': '1001110', ',': '1001111', 'т': '1010', 'ч': '1011000', 'э': '1011001', 'щ': '1011010', 'ё': '1011011', 'м': '10111', ' ': '110', 'в': '11100', 'л': '11101', 'о': '1111'}
Обратная таблица соответствия:  {'0000': 'а', '00010': 'н', '00011': 'я', '001': 'е', '0100': 'р', '010100': ')', '010101': 'б', '01011': 'п', '0110': 'с', '01110': 'у', '01111': 'к', '10000': 'и', '10001': 'д', '100100': 'ц', '1001010': '(', '1001011': 'ь', '1001100': 'ы', '1001101': 'й', '1001110': 'х', '1001111': ',', '1010': 'т', '1011000': 'ч', '1011001': 'э', '1011010': 'щ', '1011011': 'ё', '10111': 'м', '110': ' ', '11100': 'в', '11101': 'л', '1111': 'о'}

Исходная строка:  отпуск по беременности и родам (проставляете только первый месяц ухода в декрет, в случае если в этом месяце сотрудник ещё работал)
Закодированная строка:  1111101001011011100110011111100101111111100101010010100001101110010001000010111101101010100001101000011001001111100010000101111101001010010110100111101101010000011100111010001100110100011101010111111101100101101111111111001011001010011100100110010011011101011100101100001110010011001110100111011111000100001101110011010001001011110100001101010011111101110011001101110101110101100000000011100010110111011000011011100110101100110101111101111101011100101100001110010000111001101111101001000111010001000101000001111110001101101010110111100100000001010111111010000011101010100
Раскодированная строка:  отпуск по беременности и родам (проставляете только первый месяц ухода в декрет, в случае если в этом месяце сотрудник ещё работал)
"""
