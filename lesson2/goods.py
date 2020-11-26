goods = []
count = 0
user_input = int(input("Какое количество товаров вы хотите добавить?: "))
while count < user_input:
    count += 1
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    quantity = input("Введите количество товара: ")
    unit = input("Введите единицу измерения товара: ")
    temp_dic = {"название": name, "цена": price, "количество": quantity, "единица": unit}
    temp_tuple = (count, temp_dic)
    goods.append(temp_tuple)
    print("Товар добавлен.")
for element in goods:
    print(element)

analytics = {"название": [], "цена": [], "количество": [], "единица": []}
for num, goods_dic in goods:
    for key, val in goods_dic.items():
        analytics[key].append(val)
print("Ваши товары:")
for key, val in analytics.items():
    print(key, val)
