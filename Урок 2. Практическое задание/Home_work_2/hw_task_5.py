count_col = 0
tabl = ''
for el in range(32, 128):
    if count_col < 9:
        tabl += f'{el} - {chr(el)} '
    else:
        count_col = 0
        tabl += f'{el} - {chr(el)} \n'
    count_col += 1

print(tabl)
