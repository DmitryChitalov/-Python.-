arr = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
arr_negative = []
for i in arr:
    if i <0:
        arr_negative.append(i)

arr_negative.sort()
print("максимальный отрицательный элемент",end=": ")
print(arr_negative[-1])