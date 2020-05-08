from guppy import hpy

h = hpy()


def task_eight():
    a = [[int(input(f"Введите элемент массива a{j + 1}{i + 1}:")) for j in range(4)] for i in range(4)]
    for i in range(len(a)):
        num = 0
        for j in range(len(a)):
            num += a[i][j]
        a[i].append(num)
    for row in a:
        print(*row)


task_eight()
print(h.heap())
"""
Partition of a set of 35858 objects. Total size = 4044359 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  10216  28   914207  23    914207  23 str
     1   9030  25   660304  16   1574511  39 tuple                  //Работа с массивами
     2   2358   7   340968   8   1915479  47 types.CodeType         //почему то не показывает использование int данных
     3    437   1   329736   8   2245215  56 type                   //а так, как и ожидалось довольно много места занимает
     4   4581  13   324109   8   2569324  64 bytes                  //tuple(кортежи) при работе с массивами
     5   2153   6   292808   7   2862132  71 function
     6    437   1   240472   6   3102604  77 dict of type
     7     92   0   150688   4   3253292  80 dict of module
     8    236   1   109432   3   3362724  83 dict (no owner)
     9   1122   3    89760   2   3452484  85 types.WrapperDescriptorType
"""
