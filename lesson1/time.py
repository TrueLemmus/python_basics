user_input = int(input("Введите время в секундах:"))
# converting seconds into minutes
minutes = user_input // 60
# remainder of the transfer is equal to the number of seconds
seconds = user_input % 60
# converting minutes into hours
hours = minutes // 60
# remainder of the transfer is equal to the number of minutes
minutes = minutes % 60
# display the results obtained using string formatting
print("%02d:%02d:%02d" % (hours, minutes, seconds))
