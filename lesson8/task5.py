'''
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
'''


'''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''


class Warehouse:
    def __init__(self):
        self.storage = []

    def add(self, equipments):
        self.storage.extend(equipments)

    def transfer(self, index, departament_name):
        item: OfficeEquipment = self.storage[index]
        item.department = departament_name

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

