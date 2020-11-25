user_input = int(input("Введите число:"))
# converting intro str
user_input_str = str(user_input)
# add lines (скливаем строки)
user_input_str_1 = user_input_str + user_input_str
user_input_str_2 = user_input_str_1 + user_input_str
# translate strings into numbers and calculate the sum
n_sum = user_input + int(user_input_str_1) + int(user_input_str_2)
print(user_input_str, "+", user_input_str_1, "+", user_input_str_2, "=", n_sum)
