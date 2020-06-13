num = int(input())
num = str(num)
answ = ''
for idx in range(len(num) - 1, -1, -1):
    answ += num[idx]
answ = int(answ)
print(answ)
