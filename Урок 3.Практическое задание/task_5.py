
import random

a = []
b = []
for i in range(10):
    a.append(random.randrange(-50, 50))
print(a)
for i in a:
    if i < 0:
        b.append(i)
    else:
        i += 1
print(f'Максимальный отрцательный элемент в данном массиве = {max(b)}, его индекс {a.index(max(b))}')
