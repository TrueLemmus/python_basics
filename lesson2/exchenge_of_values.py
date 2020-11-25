random_list = input("Введите несколько элементов списка разделённых запятой:").split(", ")
print(f'Ваш список: {random_list}')
counter = 0
for index in range(int(len(random_list) / 2)):
    random_list[counter], random_list[counter+1] = random_list[counter+1], random_list[counter]
    counter += 2
print(f'Ваш список в которм соседние элементы заменены местами: {random_list}')
