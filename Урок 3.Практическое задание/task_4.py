"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
a = [2, 4, 2, 2, 6, 7, 9]
res_count = 0
res_num = 0
list_num = []
for i in range(0, len(a)):
    count = 1
    for j in range(0, len(a)):
        if a[i] == a[j] and i != j:
            count += 1
    if count == res_count:
        list_num.append(a[i])
    elif count > res_count:
        list_num = []
        list_num.append(a[i])
        res_count = count
if res_count == 1:
    print("все элементы уникальны")
else:
    print(
        f"Числа {', '.join(map(str, set(list_num)))} имеют {res_count} повторений")
# с функцией max не понял как делать
