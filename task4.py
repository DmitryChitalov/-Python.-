# Написать программу, которая генерирует в указанных пользователем границах
# -случайное целое число,
# -случайное вещественное число,
# -случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# случайное целое число
from random import randint
inp_str = input('Please provide 2 integer values separated by space: ').lstrip().rstrip()
val1, val2 = inp_str.split(' ') 
val1 = int(val1)
val2 = int(val2)
if val1 > val2:
    val1, val2 = val2, val1
print(f'Random integer is: {randint(val1, val2)}')

# случайное вещественное число
from random import uniform
inp_str = input('Please provide 2 decimal values separated by space: ').lstrip().rstrip()
val1, val2 = inp_str.split(' ') 
val1 = float(val1)
val2 = float(val2)
if val1 > val2:
    val1, val2 = val2, val1
print(f'Random integer is: {uniform(val1, val2)}')

from random import randint
# случайный символ вариант 1
inp_str = input('Please provide 2 lowercase English alphabet letters separated by space: ').lstrip().rstrip()
val1, val2 = inp_str.split(' ') 
code1 = ord(val1)
code2 = ord(val2)
if code1 > code2:
    code1, code2 = code2, code1
if code1 >122 or code1 < 97:
    print (f'Error. {val1} is not lowercase English alphabet letters') 
elif code2 >122 or code2 < 97:
    print (f'Error. {val2} is not lowercase English alphabet letters') 
else:
    print(f'Random symbol is: {chr(randint(code1, code2))}')

from random import randint
# случайный символ вариант 2
inp_str = input('Please provide 2 lowercase English alphabet letters separated by space: ').lstrip().rstrip()
val1, val2 = inp_str.split(' ') 
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
indx1 = ascii_lowercase.find(val1)
indx2 = ascii_lowercase.find(val2)
if indx1 > indx2:
    indx1, indx2 = indx2, indx1
if indx1 == -1:
    print (f'Error. {val1} is not lowercase English alphabet letters') 
elif indx2 == -1:
    print (f'Error. {val2} is not lowercase English alphabet letters') 
else:
    print(f'Random symbol is: {ascii_lowercase[randint(indx1, indx2)]}')

