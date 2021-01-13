"""
Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться
с ошибкой.
"""


class MyZeroDivisionError(Exception):

    @classmethod
    def alert(cls):
        return f"Деление на ноль запрещено"


while True:
    try:
        dividend, divider = map(int, input("Введите делимое и делитель через пробел: ").split())
        if divider == 0:
            raise MyZeroDivisionError
        print(dividend / divider)
    except MyZeroDivisionError:
        print(MyZeroDivisionError.alert())
