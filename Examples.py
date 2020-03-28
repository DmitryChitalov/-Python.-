# Реверс массива

NUMS = input("Введите число: ")
NUMS = NUMS.split()
NUMS = [int(i) for i in NUMS]

for i in range(len(NUMS)//2):
    print(i)
    b = NUMS[i]
    NUMS[i] = NUMS[len(NUMS)-i-1]
    NUMS[len(NUMS)-i-1]=b
print(NUMS)