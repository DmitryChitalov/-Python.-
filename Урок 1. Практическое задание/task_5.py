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


class StackOfPlates:
    def __init__(self, capacity):
        self.plates = []
        if capacity < 1:
            raise NameError('If you have zero plates it is not even a stack, dude')
        else:
            self.capacity = capacity

    def is_empty(self):
        return self.plates == []

    def push_in(self, plate):
        if self.plates == []:
            self.plates.append([plate])
        else:
            if len(self.plates[-1]) >= self.capacity:
                self.plates.append([plate])
            else:
                self.plates[-1].append(plate)

    def pop_out(self):
        if self.plates == []:
            raise NameError("Cannot pop an empty stack")
        else:
            popped_data = self.plates[-1][-1]
            if len(self.plates[-1]) == 1:
                del self.plates[-1]
            else:
                del self.plates[-1][-1]
            return popped_data

    def pop_at(self, index):
        if self.plates == []:
            raise NameError('You cannot pop an empty stack of plates')
        elif index - 1 > len(self.plates):
            raise NameError("Index is out of range")
        else:
            popped_data = self.plates[index - 1][-1]
            if len(self.plates[index - 1]) == 1:
                del self.plates[-1]
            elif len(self.plates) == index:
                del self.plates[-1][-1]
            else:
                self.plates[index - 1][-1] = self.plates[index][0]

                for i in range(index, len(self.plates)):
                    for j in range(0, len(self.plates[i]) - 1):
                        self.plates[i][j] = self.plates[i][j + 1]
                    if i < len(self.plates) - 1:
                        self.plates[i][-1] = self.plates[i + 1][0]
                del self.plates[-1][-1]
                if len(self.plates[-1]) == 0:
                    del self.plates[-1]
        return popped_data

    def get_last_plate(self):
        return self.plates[len(self.plates) -1]

    def stack_size(self):
        return len(self.plates)



if __name__ == '__main__':

    SOP = StackOfPlates(4)

    SOP.push_in(1)
    SOP.push_in(2)
    SOP.push_in(3)
    SOP.push_in(4)
    SOP.push_in(5)
    SOP.push_in(6)
    SOP.push_in(7)
    SOP.push_in(8)
    SOP.push_in(9)
    SOP.push_in(10)

    print(SOP.is_empty())

    print(SOP.stack_size())

    print(SOP.get_last_plate())

    print(SOP.plates)
