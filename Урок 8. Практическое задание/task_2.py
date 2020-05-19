"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque

#2
def tree_2(text):
    count = Counter(text)
    sort_str = deque(sorted(count.items(), key=lambda item: item[1]))
    while len(sort_str) > 1:
        dict = ((sort_str[0][0], sort_str[1][0]), sort_str[0][1] + sort_str[1][1])
        if sort_str[-1][1] < dict[1]:
            sort_str.append(dict)
        else:
            for i in range(2, len(sort_str)):
                if sort_str[i][1] >= dict[1]:
                    break
            sort_str.insert(i, dict)
        sort_str.popleft()[0]
        sort_str.popleft()[0]
    return sort_str[0][0]

#3
def code_3(st, el):
    global haf
    if type(el) == str:
        haf.append((el, st))
        return
    code_3(st + '0', el[0])
    code_3(st + '1', el[1])
    return

# 1
def dict_1(text):
    global haf
    ls = tree_2(text)
    haf = []
    code_3(' ', ls)
    dict_haf = dict(haf)
    return dict_haf

#4
def coding(text, dict_haf):
    st_res = ''
    for ch in text:
        st_res += dict_haf[ch]
    return st_res


text = "Happy New Year!"

dict_haf = dict_1(text)
coding_text = coding(text, dict_haf)

print(f'Обычный текст: {text}')
print(f'Кодированный текс: {coding_text}')

