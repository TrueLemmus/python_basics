'''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''


class MyIntError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Warehouse:
    def __init__(self):
        self.storage = []

    def add(self, equipments):
        self.storage.extend(equipments)

    def transfer(self, index, departament_name):
        try:
            if index > len(self.storage) or index < 0:
                raise MyIntError(f'Неверный индекс')
            item: OfficeEquipment = self.storage[index]
            item.department = departament_name
        except MyIntError:
            print(f'Неверный нндекс')

    def __str__(self):
        string = f'Список устройств:'
        for i in range(len(self.storage)):
            string += f'\n'
            string += f'Индекс: {i}. {self.storage[i]}'
        return string


class OfficeEquipment:

    def __init__(self,  name="str", price=0, eq_type=None):
        self.type = eq_type
        self.name = name
        self.price = price
        self.department = "Склад"

    @classmethod
    def create(cls, **properties):
        return [cls(**properties)]

    def __str__(self):
        return f"Тип: {self.type}. Название: {self.name}. Цена: {self.price}. Находится: {self.department}"


class Printer(OfficeEquipment):

    def __init__(self, **kwargs):
        super().__init__(eq_type="printer", **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type="scanner", **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type="xerox", **kwargs)


storage = Warehouse()
storage.add(Printer.create(name="Epson", price=1000))
storage.add(Scanner.create(name="Cannon", price=900))
storage.add(Xerox.create(name="Xerox", price=2000))

print(storage)
print(f'Предаём сканер в бухгалтерию')
storage.transfer(1, "Бухгалтерия")
print(storage)
print(f'Пробуем передать устройство с неверным индексом')
storage.transfer(10, "Вальгала")
