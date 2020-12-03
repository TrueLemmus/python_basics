#  данный код как по мне один сплошной костыль, тем не менее он работает
def my_func(x, y):
    x = int(x)
    y = int(y)
    if y < 0:
        y_abs = abs(y)
        count = 1
        x_temp = 0
        while count != y_abs:
            count += 1
            x_temp = x_temp + x * x
        return 1 / x_temp
    else:
        count = 1
        x_temp = 0
        while count != y:
            count += 1
            x_temp = x_temp + x * x
        return x_temp


print(my_func(input("Введите число х: "), input("Введите число y: ")))
