my_list = [7, 5, 3, 3, 2]
while True:
    user_input = int(input('Введите натуральное число: '))
    max_value = max(my_list)
    if user_input > max_value:
        my_list.insert(0, user_input)
    elif user_input in my_list:
        my_list.insert(my_list.index(user_input), user_input)
    else:
        my_list.append(user_input)
    print(f'Итоговый список: {my_list}')
