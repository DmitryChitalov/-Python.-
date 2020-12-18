# Пользователь вводит две буквы. 
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# Вариант 1
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
    print(f'Symbol [ {val1} ] is on pos {indx1 + 1}')
    print(f'Symbol [ {val2} ]is on pos {indx2 + 1}')
    print(f'Distance between symbol {val1} and symbol {val2} is {indx2 - indx1}')

# Вариант 2
mincode = 97
maxcode = 122
inp_str = input('Please provide 2 lowercase English alphabet letters separated by space: ').lstrip().rstrip()
val1, val2 = inp_str.split(' ') 
code1 = ord(val1)
code2 = ord(val2)
if code1 > code2:
    code1, code2 = code2, code1
if code1 < mincode or code1 > maxcode:
    print (f'Error. {val1} is not lowercase English alphabet letters') 
elif code2 < mincode or code2 > maxcode:
    print (f'Error. {val2} is not lowercase English alphabet letters') 
else:
    print(f'Symbol [ {val1} ] is on pos {code1 - mincode +1}')
    print(f'Symbol [ {val2} ]is on pos {code2 - mincode +1}')
    print(f'Distance between symbol {val1} and symbol {val2} is {code2 - code1}')