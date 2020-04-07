from collections import deque

class HexNum:
    def __init__(self, x):
        self.x = x
        
        
    def __str__(self):
        '''Что-то не работает, по логике этот метод должен выводить результат'''
        return (f'{self.x}: X')

       
    def __add__(self, y):
        # return ('%X' %(int(self.x, 16) + int(y.x, 16)))
        return f'{(int(self.x, 16) + int(y.x, 16)): X}'
    
    def __mul__(self, y):
        return f'{(int(self.x, 16) * int(y.x, 16)): X}'

a = HexNum(input('Введите 1-е шестнадцатиричное число: ').upper())
b = HexNum(input('Введите 2-е шестнадцатиричное число: ').upper())

print(a+b)
print(a*b)