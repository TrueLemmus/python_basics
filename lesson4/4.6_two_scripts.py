'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''
from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(random_list, iteration):
    i = 0
    iter = cycle(random_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_list = ["один", "два", "три", "четыре", "пять"]

my_count_func(start_number=int(input("Введите начальное число: ")),
              stop_number=int(input("Введите завершающее число: ")))
my_cycle_func(my_list, iteration=int(input("Введите колличество итераций: ")))
