user_input = 0
# We ask the user to enter a number and check the correctness of the input
while True:
    user_input = float(input("Введите целое положительное число:"))
    if user_input < 1:
        print("Вы ввели неверное число.")
    else:
        break
# find digits in users input and add them too list
digits = []
for symbol in str(user_input):
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
# find the greatest digit and print it
greatest = 0
for i in digits:
    if i > greatest:
        greatest = i
print("Самая большая цифра в этом числе: ", greatest)
