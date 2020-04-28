"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque

# создать дерево хафмана по тексту
def make_tree(text):
    """Функция построения дерева"""
    # строим отсортированный deque (символ, частота)
    count_ = Counter(text)
    ls = deque(sorted(count_.items(), key=lambda item: item[1]))

    # построить двоичное дерево
    while len(ls) > 1:
        d = ((ls[0][0], ls[1][0]), ls[0][1] + ls[1][1])
        if ls[-1][1] < d[1]:
            ls.append(d)
        else:
            for num in range(2, len(ls)):
                if ls[num][1] >= d[1]:
                    break
            ls.insert(num, d)
        ls.popleft()[0]
        ls.popleft()[0]
    return ls[0][0]

# рекурсивно создать бинарный код листов эелемнта
def haffman_code(st, el):
    global ls_haf
    if type(el) == str:
        ls_haf.append((el, st))
        return
    haffman_code(st + '0', el[0])
    haffman_code(st + '1', el[1])
    return

# создать словарь хаффмана по тексту
def make_dict(text):
    global ls_haf
    ls = make_tree(text)
    ls_haf = []
    haffman_code(' ', ls)
    dict_haf = dict(ls_haf)
    return dict_haf

# сжать по хаффману
def compress(text, dict_haf):
    st_res = ''
    for ch in text:
        st_res += dict_haf[ch]
    return st_res

# decompress
def decompress(text, dict_haf):
    dc_decod = {dict_haf[key]: key for key in dict_haf}
    st_res = ''
    while len(text) > 0:
        num = 1
        while text[:num] not in dc_decod:
            num += 1
        st_res += dc_decod[text[:num]]
        text = text[num:]
    return st_res


text = "beep boop beer!"

dict_haf = make_dict(text)
compressed_text = compress(text, dict_haf)
decompressed_text = decompress(compressed_text, dict_haf)

print(f'Text : {text}')
print(f'Compress tex : {compressed_text}')
print(f'Decompressed text : {decompressed_text}')

wright_answer = ' 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001'

if wright_answer == compressed_text:
    print("It's OK")
else:
    print('Work hard!')

