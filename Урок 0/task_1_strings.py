"""
Substitution into the strings
"""

ST = "Привет я строка"
print(ST)

TEMPLATE = "Привет я шаблон первый=%d & второй=%d | третий=%d"
print(TEMPLATE)
RESULT = TEMPLATE % (1, 2, 3)
print(RESULT)

print("Или коротко %d %d" % (1, 2))

A = 1
B = 2
C = A + B
TEMPLATE = "result = %d"
RESULT = TEMPLATE % C

RESULT = "result = %d" % (A + B)
