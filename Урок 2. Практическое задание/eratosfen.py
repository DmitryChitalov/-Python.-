NUMBER = int(input("Вывод простых чисел до числа: "))
WORK_LIST = [0] * NUMBER  # создание массива с n количеством элементов
for i in range(NUMBER):  # заполнение массива ...
    WORK_LIST[i] = i  # значениями от 0 до n-1

# вторым элементом является единица, которую не считают простым числом
# забиваем ее нулем.
WORK_LIST[1] = 0

for el in WORK_LIST:
    if el == 0:
        continue
    else:
        for j in WORK_LIST[el+1:]:
            if j != 0 and j % el == 0:
                WORK_LIST[j] = 0
RES_LIST = []
for el in WORK_LIST:
    if el != 0:
        RES_LIST.append(el)
print(RES_LIST)
