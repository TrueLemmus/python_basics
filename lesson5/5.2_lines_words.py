'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

with open("5.2.txt") as f:
    data = f.readlines()

lines = len(data)

print(f"В файле {lines} строк(а/и)")

i = 1
for line in data:
    words = len(line.split())
    print(f"В {i} строке {words} слов(о/а)")
    i += 1



