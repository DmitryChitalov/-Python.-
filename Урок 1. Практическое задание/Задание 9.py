NUM1 = int(input("Введите первое число: "))
NUM2 = int(input("Введите второе число: "))
NUM3 = int(input("Введите третье число: "))
if NUM3 < NUM1 and  NUM1 < NUM2:
    print(f"Средним числом является {NUM1}")
elif NUM2 < NUM3 and NUM3 < NUM1:
    print(f"Средним числом является {NUM3}")
else:
    print(f"Средним числом является {NUM2}")
