
# importing Dates and Time
# 

from datetime import date, time, datetime

# today = date.today()

# print(today.day, today.month, today.year)
# print("Today's weekday is: ", today.weekday())

# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print("Today's Weekday Day is: ", days[today.weekday()])


today = datetime.now()
print("Current date and time is: ", today)

t = datetime.time(datetime.now())
print(t)

