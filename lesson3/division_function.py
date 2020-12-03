# division function of two numbers
def div_func(a, b):
    # Replaced a comma to a point
    a = float(a.replace(',', '.'))
    b = float(b.replace(',', '.'))

    if b == 0:
        return "Деление на ноль невозможно"
    else:
        result = a / b
        return result


c = div_func(input("Ввдедите делимое число: "), input("Ввдедите число делитель: "))
if c is float:
    print(f'Результат деления {c}')
else:
    print(c)
