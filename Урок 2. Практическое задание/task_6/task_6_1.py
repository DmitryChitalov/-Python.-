"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import random
numbergame = int(random.randint(1,100))
attempt = 10
numberusers = int(input("я загадал число от 1 до 100 попробуйте отгадать, у вас 10 попыток--"))
while attempt > 1:
    if numberusers == numbergame:
        print("молодец отгада, число было загадано число", numbergame)
        break
    elif numberusers > numbergame:
        attempt -= 1
        print("ты ввел больше загаданного числа")
        numberusers = int(input(f"попробуй еще раз, у вас {attempt} попыток--"))
    elif numberusers < numbergame:
        attempt -= 1
        print("ты ввел меньше загаданного числа")
        numberusers = int(input(f"попробуй еще раз, у вас {attempt} попыток--"))
if numberusers == numbergame:
    print("конец игре")
else:
    print("попытки кончились, загаданно число ", numbergame)

