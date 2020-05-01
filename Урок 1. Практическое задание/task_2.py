"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

NUM_1 = 5  # 101
NUM_2 = 6  # 110

print(f"Даны числа {NUM_1} и {NUM_2}")

# логическое И
print(f"Логическое 'И': {NUM_1} & {NUM_2} = {NUM_1 & NUM_2} ")

# логическое ИЛИ
print(f"Логическое 'ИЛИ': {NUM_1} | {NUM_2} = {NUM_1 | NUM_2} ")

# логическое ИСКЛЮЧАЮЩЕЕ ИЛИ
print(f"Логическое 'ИСКЛЮЧАЮЩЕЕ ИЛИ': {NUM_1} ^ {NUM_2} = {NUM_1 ^ NUM_2} ")

# логическое ОТРИЦАНИЕ
print(f"Логическое 'ОТРИЦАНИЕ': ~{NUM_1} = {~NUM_1} \n ~{NUM_2} = {~NUM_2} ")

# логический сдвиг вправо на два знака
print(f"Логический сдвиг вправо на два знака: {NUM_1} >> 2 = {NUM_1 >> 2}")

# логический сдвиг влево на два знака
print(f"Логический сдвиг влево на два знака: {NUM_1} << 2 = {NUM_1 << 2}")
