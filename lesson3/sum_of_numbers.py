def sum_of_numbers():
    numbers_sum = 0
    exit_init = 0
    while True:
        numbers = input('Введите несколько чисел через пробел или "exit" для завершения: ')
        numbers = numbers.split(" ")
        for i in numbers:  # ищем и удаляем пустые элементы списка
            if "" == i:
                numbers.remove("")
        for i in numbers:  # ищем слово exit среди списка, делаем это отдельно потому что пустые элементы каким то образом мешают
            if "exit" == i:
                numbers.remove("exit")
                exit_init = 1
        numbers = map(int, numbers)
        numbers_sum += sum(numbers)
        print(numbers_sum)
        if exit_init == 1:
            break


sum_of_numbers()
