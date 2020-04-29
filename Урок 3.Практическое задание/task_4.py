"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""


M = [5, 6, 12, 3, 3, 12, 46, 3, 3, 3, 12, 12, 3, 3, 89]
print(M)

MAX_FRQ_NUM = M[0]
MAX_FRQ = 1

for i in range(len(M)-1):
    FRQ = 1
    for j in range(i+1, len(M)):
        if M[j] == M[i]:
            FRQ += 1
    if FRQ > MAX_FRQ:
        MAX_FRQ = FRQ
        MAX_FRQ_NUM = M[i]

print(MAX_FRQ_NUM)
