from collections import deque


class MathCalc:

    # длина элементарной ячейки памяти
    base_length = 4
    # количество элементов до пробела в строке
    string_max = 4
    # базоввый стек символов
    stek = "0123456789ABCDEF"
    # преобразованный стек
    stek_dict = {
        "0123456789ABCDEF"[el]: el for el in range(
            len("0123456789ABCDEF"))}

    @classmethod
    def change_base_length(cls, new_length):
        answer = input(
            "Все созданные элементы класса перестанут корректно функцианировать. Вы уверены: y/n\n")
        if answer.lower() == 'y':
            cls.base_length = new_length

    @classmethod
    def change_string_max(cls, new_string):
        cls.string_max = new_string

    @staticmethod
    def another_system(obj, new_system):

        if new_system != obj.system:
            if obj.dec is None:
                count = obj.base_count - 1
                pow_value = obj.base_count * MathCalc.base_length - 1
                dec = 0
                while count >= 0:
                    for i in range(MathCalc.base_length):
                        tmp = MathCalc.stek_dict[obj.value[count][i]]
                        dec += tmp * pow(obj.system, pow_value)
                        pow_value -= 1
                    count -= 1
                obj.dec = dec
            else:
                dec = obj.dec

            new_value = {0: ['0' for i in range(MathCalc.base_length)]}
            index = 1
            count = 0
            start = True
            while dec != 0:
                if start:
                    start = False
                else:
                    dec = dec // new_system
                el = dec % new_system
                if index == MathCalc.base_length + 1 and dec != 0:
                    index = 1
                    count += 1
                    new_value[count] = [
                        '0' for i in range(
                            MathCalc.base_length)]
                if index < MathCalc.base_length + 1:
                    new_value[count][-index] = MathCalc.stek[el]
                    index += 1

                obj.system = new_system
                obj.value = new_value
                obj.base_count = count + 1

    def __init__(self, str_data, system=10):

        if isinstance(str_data, str):
            self.base_count = (len(str_data) // MathCalc.base_length) + 1
            length = len(str_data)
            self.value = {i: ['0' for i in range(
                MathCalc.base_length)] for i in range(self.base_count)}
            count = 0
            for i in range(1, length + 1):
                tmp = i % MathCalc.base_length
                if tmp == 0:
                    self.value[count][-MathCalc.base_length] = str_data[-i]
                    count += 1
                else:
                    self.value[count][-tmp] = str_data[-i]
        elif isinstance(str_data, dict):
            self.base_count = len(str_data)
            self.value = str_data
        else:
            print("Need string for initialization")
        self.system = system
        self.dec = None if system != 10 else int(str_data)

    def __str__(self):

        count = self.base_count - 1
        string = ''
        string_count = 0
        while count >= 0:
            null = False
            if self.value[count][0] == '0':
                null = True

            for i in range(MathCalc.base_length):
                if self.value[count][i] == '0' and null:
                    pass
                else:
                    string += self.value[count][i]
                    string_count += 1
                    if string_count == MathCalc.string_max:
                        string += ' '
                        string_count = 0
            count -= 1
        return f"{string}"

    def __add__(self, other):

        if self.system == other.system:
            base_max = max(self.base_count, other.base_count)
            result = {i: ['0' for i in range(MathCalc.base_length)]
                      for i in range(base_max)}
            next = 0
            for i in range(base_max):
                if self.value.get(i) is None:
                    a_i = ['0' for i in range(MathCalc.base_length)]
                    b_i = other.value[i]
                elif other.value.get(i) is None:
                    a_i = self.value[i]
                    b_i = ['0' for i in range(MathCalc.base_length)]
                else:
                    a_i = self.value[i]
                    b_i = other.value[i]

                for j in range(1, MathCalc.base_length + 1):

                    tmp = (MathCalc.stek_dict[a_i[-j]] +
                           MathCalc.stek_dict[b_i[-j]])
                    current = tmp % self.system
                    result[i][-j] = MathCalc.stek[current + next]
                    next = tmp // self.system
                if next != 0:
                    result[i + 1][-1] = MathCalc.stek[next]

            if next != 0:
                result[base_max] = ['0' for i in range(MathCalc.base_length)]
                result[base_max][-1] = MathCalc.stek[next]

            return MathCalc(result, self.system)

    def __mul__(self, other):

        if self.system == other.system:
            pr_sys = self.system
            MathCalc.another_system(self, 10)
            MathCalc.another_system(other, 10)
            new_el = MathCalc(f"{self.dec*other.dec}", 10)
            MathCalc.another_system(new_el, pr_sys)
            MathCalc.another_system(self, pr_sys)
            MathCalc.another_system(other, pr_sys)

            return new_el


class MathDeque:
    # базоввый стек символов
    stek = "0123456789ABCDEF"
    # преобразованный стек
    stek_dict = {
        "0123456789ABCDEF"[el]: el for el in range(
            len("0123456789ABCDEF"))}

    @staticmethod
    def convert_to_dec(obj):
        pow_value = len(obj.value) - 1
        dec = 0
        for el in obj.value:
            tmp = MathDeque.stek_dict[el]
            dec += tmp * pow(obj.system, pow_value)
            pow_value -= 1
        return dec

    @staticmethod
    def another_system(obj, new_system):

        if obj.system != new_system:

            new_value = deque()
            dec = obj.dec
            new_value.appendleft(MathDeque.stek[dec % new_system])
            dec = dec // new_system
            while dec != 0:
                new_value.appendleft(MathDeque.stek[dec % new_system])
                dec = dec // new_system

            obj.value = new_value
            obj.system = new_system

    def __init__(self, str_data, system=10):

        if isinstance(str_data, str):
            self.value = deque(str_data)
            self.system = system
            self.dec = MathDeque.convert_to_dec(self)

    def __str__(self):
        return f"{self.value}"

    def __add__(self, other):

        if self.system == other.system:

            value = str(self.dec + other.dec)
            new_el = MathDeque(value)
            MathDeque.another_system(new_el, self.system)

            return new_el

    def __mul__(self, other):

        if self.system == other.system:

            value = str(self.dec * other.dec)
            new_el = MathDeque(value)
            MathDeque.another_system(new_el, self.system)

            return new_el
