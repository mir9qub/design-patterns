# S (The Single Responsibility Principle) – принцип единой ответственности
# то есть один класс решает одну задачу и у класса должна быть только одна причина для изменения.


# хранение и удаление записи основная обязанность журнала
class Journal:
    def __init__(self):
        self.count = 0
        self.entries = []

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    """
    Но если добавить еще обязанности: Сохранить в файл, загрузить из файла, загрузить из веб-ресурса то 
    мы нарушаем принцип единственной ответсвенности.
    Не стоит перегружать свои объекты слишком большим количеством обязанностей.
    и это можно назвать антипаттерном <Всемогущий объект>
    """
    """ def save(self, filename):
        with open(filename) as f:
            f.write(str(self))

    def load(self, filename):
        pass

    def low_from_web(self, uri):
        pass
    """

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')
""" Output:
Journal entries:
1: I cried today.
2: I ate a bug.
"""

