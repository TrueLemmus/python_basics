def my_func(x, y, z):
    arg_list = [x, y, z]
    largest_arg = []
    for i in range(len(arg_list) - 1):
        largest_arg.append(max(arg_list))
        arg_list.remove(max(arg_list))
    print(f'Сумма двух наибольших чисел: {sum(largest_arg)}')


my_func(int(input("Введите число X: ")), int(input("Введите число Y: ")), int(input("Введите число Z: ")))
