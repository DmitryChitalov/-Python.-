"""
Задание 7.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def append(self, item):
        self.elems.append(item)

    def extract(self, indx):
        return self.elems.pop(indx)

    def size(self):
        return len(self.elems)
    
    def __str__(self):
        return str([elem for elem in self.elems])

if __name__ == '__main__':
    queue_main = QueueClass() # Главная 
    queue_done = QueueClass() # Выполненные задачи
    queue_change = QueueClass() # Требуется корректировка
    
    # Loading tasks into queue_main
    import random as rnd
    for i in range(0, 21):
        queue_main.append(rnd.randint(1, 100))
    
    # Moving tasks from queue_main to queue_done if task has been done
    for i in range(0, 20, 2):
        if queue_main.size() <= i:    
            break
        elif queue_main.is_empty() != True:
            queue_done.append(queue_main.extract(i))
        else:
            print(f'Main queue is empty')

    # Moving tasks from queue_main to queue_change if task required review
    for i in range(0, 20, 2):
        if queue_main.size() <= i:    
            break
        elif queue_main.is_empty() != True:
            queue_change.append(queue_main.extract(i))
        else:
            print(f'Main queue is empty')
    
    # Check if everuthing was done
    if queue_main.is_empty() == True:
        print(f'Your main queue is empty')
        if queue_change.is_empty() == True:
            print(f'Congratulation you have solved all your tasks')
        else:
            print(f'You have tasks for review {queue_change}')
    else:
        print(f'Your have not solved {queue_main.size()} tasks')
        print(f'Thare are all {queue_main}')
        print(f'Your have solved {queue_done} tasks')
        print(f'Thare are task for review {queue_change}')





    


