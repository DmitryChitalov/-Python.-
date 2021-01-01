"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
import timeit

us_dict = {'z' : 2, 'b' : 8, 'c' : 10, 'd' : 12, 'a' : 45}
or_dict = OrderedDict()
or_dict = {'z' : 2, 'b' : 8, 'c' : 10, 'd' : 12, 'a' : 45}

def us_dict_update(key, val):
    us_dict.update({key : val})

def or_dict_update(key, val):
    or_dict.update({key : val})


key = 'r'
val = 888
print(timeit.timeit("us_dict_update(key, val)", setup="from __main__ import us_dict_update, key, val", number=1000))
print(timeit.timeit("or_dict_update(key, val)", setup="from __main__ import or_dict_update, key, val", number=1000))
"""
0.00022180000000000116
0.0002420999999999951
"""
# Время обновления почти одинаково


def us_dict_get(key):
    return us_dict.get(key)

def or_dict_get(key):
    return or_dict.get(key)


key = 'a'
print(timeit.timeit("us_dict_get(key)", setup="from __main__ import us_dict_get, key", number=1000))
print(timeit.timeit("or_dict_get(key)", setup="from __main__ import or_dict_get, key", number=1000))
"""
0.00011160000000000336
0.00011830000000000174
"""
# Время выполнения get почти одинаково

# Я не вижу преимуществ у OrderedDict
