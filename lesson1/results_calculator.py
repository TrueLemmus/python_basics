a = int(input("Сколько километров пробежал спортсмен в перый день?: "))
b = int(input("Сколько километров спортсмен должен пробежать?: "))
count = 1
while a <= b:
    print(count, "-й день:", a)
    a = round(a * 1.1, 2)
    count = count + 1
print("На", count, "-й день спортсмен достигнет результата — не менее", a, "км")
