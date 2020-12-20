"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class StackClass:
    def __init__(self, size):
        self.size = size
        self.curr_size = 0
        self.elems = []

    def push(self, el):
        if self.curr_size == self.size:
            return False
        self.elems.append(el)
        self.curr_size += 1
        return True

    def pop(self):
        self.curr_size -= 1
        return self.elems.pop()

    def get(self, indx):
        if indx >= self.get_size():
            return None
        else:
            return self.elems[indx]

    def get_size(self):
        return len(self.elems)

    def __str__(self):
        return str([elem for elem in self.elems])

if __name__ == '__main__':
# Fill stacks
    import random as rnd
    SC_OBJ = [] # Stack array
    SC_OBJ.append(StackClass(2))
    indx = 0
    for num in range(0, 30):
        if SC_OBJ[indx].push(rnd.randint(1, 100)) == False:
            SC_OBJ.append(StackClass(2))
            indx += 1
        else:
            SC_OBJ[indx].push(rnd.randint(1, 100))
# Read stacks and every component 
    for el in SC_OBJ:
        print(el)
        for indx in range(0, el.get_size()):
            print(el.get(indx))
        

