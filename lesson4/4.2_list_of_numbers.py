'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''

def more_previous(random_list):
    for i in range(1, len(random_list)):
        if random_list[i] > random_list[i-1]:
            yield random_list[i]


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = (my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1])

print(list(more_previous(my_list)))
print(list(new_list))
