str = "Привет я строка"
print(str)

template = "Привет я шаблон первый=%d & второй=%d | третий=%d"
print(template)
result = template % (1,2,3)
print(result)

print("Или коротко %d %d" % (1, 2))



A = 1
B = 2
C = A + B
template = "result = %d"
result = template % C

result = "result = %d" % (A + B)
