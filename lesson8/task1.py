'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Date:

    cls_date = []
    day = 0
    month = 0
    year = 0

    def __init__(self, date):
        Date.cls_date = date.split('-')

    @classmethod
    def to_int(cls):
        Date.day = int(Date.cls_date[0])
        Date.month = int(Date.cls_date[1])
        Date.year = int(Date.cls_date[2])
        return f'День {Date.day}, тип {type(Date.day)}\n'\
               f'Месяц {Date.month}, тип {type(Date.month)}\n'\
               f'Год {Date.year}, тип {type(Date.year)}'

    @staticmethod
    def valid():
        if Date.day >= 32:
            return f'Неверный день'
        if Date.month >= 13:
            return f'Неверный месяц'
        if Date.year >= 2030:
            return f'Неверный год'
        return f'Всё верно'


user_date = Date(input(f'Введите дату через тире "день-месяц-год": '))
print(Date.to_int())
print(Date.valid())
