import calendar


# Creat a plain text calendar

caldr = calendar.TextCalendar(calendar.SUNDAY)
# frmt = caldr.formatmonth(2021, 1, 0, 0)
# print(frmt)

"""
# Creat a plain HTML calendar

caldr = calendar.HTMLCalendar(calendar.SUNDAY)
frmt = caldr.formatmonth(2021, 1, 0, 0)
print(frmt)

"""
for i in caldr.itermonthdates(2017, 8):
    print(i)







