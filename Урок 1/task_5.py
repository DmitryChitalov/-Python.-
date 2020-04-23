MIN = ord(input("Нижняя буква: "))
MAX = ord(input("Вверхняя буква: "))

print(f"Место первой: {MIN - ord('a')+1}")
print(f"Место второй: {MAX - ord('a')+1}")
print(f"Между ними: {MAX - MIN - 1}")
input("Press any to exit...")