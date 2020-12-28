'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

numbers = "10 12 18 1 5 30 14 20"  # можно заменить на запрос ввода у пользователя

with open('5.5.txt', 'a') as f:  # каждый запуск скрипта добавляет строчку
    f.write(f'\n{numbers}')

with open('5.5.txt', 'r') as f:
    file_numbers = f.read()

file_numbers = file_numbers.split()
file_numbers = map(int, file_numbers)
file_numbers = sum(file_numbers)

print(file_numbers)

