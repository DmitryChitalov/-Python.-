def ert(l, b):
    if l < n:  # перебор всех элементов до заданного числа
        if b[l] != 0:  # если он не равен нулю, то
            j = l * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                b[j] = 0  # заменить на 0
                j = j + l  # перейти в позицию на m больше
        l += 1
        return ert(l, b)
    else:
        return b


n = int(input("вывод простых чисел до числа ... "))
a = [0] * n
for i in range(n):
    a[i] = i
a[1] = 0
m = 2
ert(m, a)
for i in a:
    if a[i] != 0:
        print(a[i], end=' ')
