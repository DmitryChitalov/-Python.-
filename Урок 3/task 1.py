num = [0,0,0,0,0,0,0,0]
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
         num[j-2]+=1

for i in num:
    print(f"{i}")