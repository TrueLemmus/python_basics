user_input = int(input('Введите порядковый номер месяца:'))
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seasons.keys():
    if user_input in seasons[key]:
        print(f'{user_input}-й месяц соответствует времени года {key}')

seasons_list = ["зима",
                "зима",
                "весна",
                "весна",
                "весна",
                "лето",
                "лето",
                "лето",
                "осень",
                "осень",
                "осень",
                "зима"]
print(f'\n{user_input}-й месяц соответствует времени года {seasons_list[user_input - 1]}')

