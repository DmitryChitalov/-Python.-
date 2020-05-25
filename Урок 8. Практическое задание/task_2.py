"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter

# string = input('Введите строку из трех слов: ') - для ввода любой другой строки
string = "beep boop beer!"

counter_list = Counter(string).items()  # считаю буквы

count_letters = sorted(counter_list, key=lambda i: i[1])  # сортирую список по возрастанию количества букв

# print(count_letters)
code_letters = dict(count_letters.copy())  # сразу формирую словарь для кодов букв из списка букв
for h in code_letters:
    code_letters[h] = ''  # зануляю значения в словаре


# print(code_letters)

def recur_tree(count_letters):  # рекурсия для построения дерева и вычисления кода букв вместе
    if len(count_letters) == 1:
        return count_letters
    else:
        for j in code_letters.keys():  # поскольку складываются первые две буквы в списке, первоему значению сразу
            # даем 0 в словаре, второму - 1цу
            if j in count_letters[0][0]:
                code_letters[j] += str(0)
            elif j in count_letters[1][0]:
                code_letters[j] += str(1)
        # print(code_letters)
        cl1 = count_letters[0][0] + count_letters[1][0]  # складываю и буквы, и числа
        cl2 = count_letters[0][1] + count_letters[1][1]
        count_letters.insert(0, (cl1, cl2))  # добавляю сложенные строку и число (узел) в массив
        sorted_cl = (sorted(count_letters, key=lambda i: i[1]))  # снова сортирую с новым элементом, чтобы узел
        # встал на новое место
        del sorted_cl[0:2]  # удаляю первые два значения, которые уже использовались
        # print(sorted_cl)

        return recur_tree(sorted_cl)


recur_tree(count_letters)
print(code_letters)

for s in string:
    print(code_letters[s][::-1], end=' ')  # поскольку посчет кода шел снизу вверх, приходится переворачивать значения
