"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""
S = str(input("Введите строку S: "))

print("Строка \'%s\' имеет длину %d символов." % (S, len(S)))

subs_set = set()
# subs_dict = {}
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))
        # print(S[i:j], i, j)
        # subs_dict[S[i:j]] = hash(S[i:j])

# print(len(list(subs_dict.keys())), list(subs_dict.keys()))
print(f"Количество различных подстрок в этой строке: {len(subs_set)}")
