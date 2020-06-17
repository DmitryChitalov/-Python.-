
answ = []

for kr in range(2,10):
    count = 0
    for el in range(2, 100):
        if el % kr == 0:
            count += 1
    answ.append(count)
for el in range(2, 10):
    print(f'В диапазоне 2-99: {answ[el-2]} чисел кратны {el} ')