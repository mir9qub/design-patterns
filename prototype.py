import copy


# Прототип — это порождающий паттерн, который позволяет копировать объекты любой сложности
# без привязки к их конкретным классам.

class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country


    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


    def __str__(self):
        return f'{self.name} lives at {self.address}'

address = Address('Abai street 1', 'Almaty', 'KZ')
john = Person('John', address)
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = 'Abai street 2'
print(john)
print(jane)

"""
Output:
John lives at Abai street 1, Almaty, KZ
Jane lives at Abai street 2, Almaty, KZ
"""