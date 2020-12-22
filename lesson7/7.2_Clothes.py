'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_count(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self._size = size

    def cloth_count(self):
        return self._size / 6.5 + 0.5

    @property
    def size_check(self):
        return self._size


class Suit(Clothes):
    def __init__(self, height):
        self._height = height

    def cloth_count(self):
        return 2 * self._height + 0.3

    @property
    def height_check(self):
        return self._height


coat = Coat(38)
suit = Suit(169)

print(f'Расход ткани на пальто {coat.cloth_count()}')
print(f'Расход ткани на пальто {suit.cloth_count()}')
print(coat.size_check)
