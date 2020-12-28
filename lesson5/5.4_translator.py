'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
data_to_write = []

with open('5.4_eng.txt', encoding='utf-8') as f1:
    lines = f1.readlines()
    for i, line in enumerate(lines, 1):
        data = line.split(" — ")
        num = data[0].strip()
        num = num.replace(num, dictionary[num])
        new_data = f"{num} — {data[1]}"
        data_to_write.append(new_data)

with open("5.4_rus.txt", "w", encoding='utf-8') as f2:
    f2.writelines(data_to_write)

print("Новый файл: 5.4_rus.txt")
