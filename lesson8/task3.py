"""
Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу
исключения на реальном примере. Необходимо запрашивать у
пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются
бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается,
сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может
вводить только числа и строки. При вводе пользователем очередного
элемента необходимо реализовать проверку типа элемента и вносить
его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение. При этом работа скрипта не должна
завершаться.
"""


class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []

while True:
    user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")
    if user_input == "stop":
        break
    try:
        if not user_input.isdigit():
            raise NotNumberError(f"'{user_input}' Не является числом")
        my_list.append(int(user_input))
    except NotNumberError as e:
        print(e)

print(my_list)
