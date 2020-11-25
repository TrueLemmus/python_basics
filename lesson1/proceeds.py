proceed = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму ваших издержек: "))
if proceed > costs:
    print("Ваша фирма отработала с прибылью")
    profit = (proceed - costs) / proceed
    print("Соотношение прибыли к выручке:", profit)
    employers = int(input("Введите количество сотрудников: "))
    profit_per_employer = (proceed - costs) / employers
    print("Прибыль фирмы в расчете на одного сотрудника: ", profit_per_employer)
else:
    print("Ваша фирма работет в убыток")
