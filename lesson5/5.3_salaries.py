'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

print("Сотрудники, получающие меньше 20000: ")
salaries = []

with open("5.3.txt", encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        salaries.append(int(words[1]))
        if int(words[1]) < 20000:
            print(words[0])

mean = float(sum(salaries)) / max(len(salaries), 1)
print(f"Средняя зарплата равняется: {mean}")
