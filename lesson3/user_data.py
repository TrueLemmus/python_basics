#  Коментарий крик души.
#  Написал функцию которая запрашивает у пользовотеля данные из списка и собирает это всё в словарь.
#  К сожалению я поздно понял что требовалось сделать совсем другое.
#  Удалять этот код не буду возможно он мне понадобится в будущем

def ask(*args):
    temp_dict = {}
    for i in range(len(args)):
        for el in args[i]:
            user_input = input(f"Введите {el}: ")
            temp_dict[el] = user_input
    return temp_dict


questions = ["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]


#  простейшая фукция которая на вход получает несколько именнованных аргументов и выводит их
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name=input("Введите ваше имя: "),
             surname=input("Введите вашу фамилию: "),
             byear=input("Введите ваш год рождения: "),
             city=input("Введите ваш город проживания: "),
             email=input("Введите ваш email: "),
             phone=input("Введите ваш номер телефона "))
