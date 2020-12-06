user_input = input("Введите строку из нескольких слов разделённых пробелами: ").split(' ')
for count in range(len(user_input)):
    if len(user_input[count]) > 10:
        user_str = user_input[count]
        print(f'{count + 1}. {user_str[:10 - len(user_input[count])]}')
    else:
        print(f'{count + 1}. {user_input[count]}')
