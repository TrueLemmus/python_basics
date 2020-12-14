'''Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

import functools


def multiplier(x, y):
    return x * y


generator = (el for el in range(100, 1001) if el % 2 == 0)
generated_list = list(generator)
print(f'Сгенирированный список:\n{list(generated_list)}')
print(f'Произведение всех элементов списка:\n{functools.reduce(multiplier, generated_list)}')
