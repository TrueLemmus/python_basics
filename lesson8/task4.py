'''
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''


class Warehouse:
    pass


class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):

    def __init__(self, name, price, quantity):
        self.type = "printer"
        super().__init__(name, price, quantity)


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity):
        self.type = "scanner"
        super().__init__(name, price, quantity)


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity):
        self.type = "xerox"
        super().__init__(name, price, quantity)


p1 = Printer('Canon', 1000, 4)
s1 = Scanner('Epson', 900, 2)
x1 = Xerox('Xerox', 1200, 1)
print(f'Тип устройства: {p1.type}. Название: {p1.name}. Цена: {p1.price} руб. Количество: {p1.quantity} шт. ')
