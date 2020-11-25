# def permutation(a, value):
#     max_value = max(a)
#     if value > max_value:
#         a.insert(0, value)
#     elif value in a:
#         a.insert(a.index(value), value)
#     else:
#         a.append(value)
#
#
# my_list = [7, 5, 3, 3, 2]
# print(my_list)
# permutation(my_list, 3)
# print(my_list)
# permutation(my_list, 8)
# print(my_list)
# permutation(my_list, 1)
# print(my_list)

my_list = [7, 5, 3, 3, 2]

while True:
    user_input = int(input('Введите натуральное число: '))
    for count in range(len(my_list) - 1, -1, -1):
        if user_input <= my_list[count]:
            my_list.insert(count + 1, user_input)
            break
    else:
        my_list.insert(count, user_input)

    print(f'Итоговый список: {my_list}')
