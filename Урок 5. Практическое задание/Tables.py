from collections import defaultdict


class DataTable:

    @staticmethod
    def type_transform(table_name, column_name, info):
        type_info = table_name.columns[column_name]
        if type_info == "int":
            table_name.total_count += int(info)
            table_name.cur_count += int(info)
            return int(info)
        elif type_info == "float":
            table_name.total_count += float(info)
            table_name.cur_count += float(info)
            return float(info)
        return info

    def __init__(self, **column_names):
        self.cur_id = 0
        self.total_count = 0
        self.cur_count = 0
        self.columns = column_names
        self.data = defaultdict(list)

    def insert_data(self):
        print("New Data")
        self.data['id'].append(self.cur_id)
        for name in self.columns:
            info = input(f"Enter {name}: ")
            info = DataTable.type_transform(self, name, info)
            self.data[name].append(info)
        self.data['total_profit'].append(self.cur_count)
        self.cur_count = 0
        self.cur_id += 1

    def print_info(self):
        print("id".rjust(10), end='')
        for name in self.columns:
            print(f"{name} ".rjust(10), end='')
        print()
        for index in self.data['id']:
            print(f"{index} ".rjust(10), end='')
            for name in self.columns:
                print(f"{self.data[name][index]}".rjust(10), end='')
            print()

    @property
    def conclusion(self):
        lower_avg = []
        upper_avg = []
        total_avg = self.total_count / self.cur_id
        print()
        print(f"Средняя годовая прибыль всех предприятий: {total_avg}")
        for index in self.data['id']:
            if self.data['total_profit'][index] >= total_avg:
                upper_avg.append(self.data['name'][index])
            else:
                lower_avg.append(self.data['name'][index])
        print("Предприятия, с прибылью выше среднего значения:")
        print(f"{upper_avg}")
        print("Предприятия, с прибылью ниже среднего значения:")
        print(f"{lower_avg}")
        del lower_avg, upper_avg

class TableTuple:

    @staticmethod
    def count_profit(tuple):
        result = 0
        for data in tuple.profit:
            result += int(data)
        return result

    def __init__(self):
        self.cur_id = 0
        self.total_count = 0
        self.data = {}

    def insert_data(self, named_tuple):
        profit = TableTuple.count_profit(named_tuple)
        self.total_count += profit
        self.data[self.cur_id] = (named_tuple, profit)
        self.cur_id += 1

    @property
    def conclusion(self):
        lower_avg = []
        upper_avg = []
        total_avg = self.total_count/self.cur_id
        print()
        print(f"Средняя годовая прибыль всех предприятий: {total_avg}")
        for id, info in self.data.items():
            if info[1] >= total_avg:
                upper_avg.append(info[0].name)
            else:
                lower_avg.append(info[0].name)
        print("Предприятия, с прибылью выше среднего значения:")
        print(f"{upper_avg}")
        print("Предприятия, с прибылью ниже среднего значения:")
        print(f"{lower_avg}")
        del lower_avg, upper_avg