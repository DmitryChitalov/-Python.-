from math import sqrt

# Алгоритм ужасен и прожорлив
MAX_NUMBER = 34565
my_array = [2]
my_array2 = []
for i in range(3, MAX_NUMBER + 1, 2):
    my_array.append(i)

for ii in range(2, round(sqrt(MAX_NUMBER))):
    for iii in my_array:
        if iii % ii != 0 or iii <= ii:
            my_array2.append(iii)
    my_array = my_array2[:]
    my_array2 = []

print(
    f'В диапазоне от 2 до {MAX_NUMBER} найдено {len(my_array)} и вот они: \n{my_array}')
