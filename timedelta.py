from datetime import date, time, datetime, timedelta, timezone
from time import localtime

print(timedelta(days=12, hours=12, minutes=45, seconds=44))

# print today's date and time

now = datetime.now()

print("Today's date and time is :", datetime.now())

print("Date after one year from now: ", str(now + timedelta(days=365)))


print("in 2 days and 3 weeks it'll be: ", str(now + timedelta(days=2, weeks=3)))



t = datetime.now() - timedelta(weeks = 1)
s = t.strftime("%A %B %d, %Y")

print("One Week Ago It Was: " + s)


today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print("April Fool's Day already went by %d days ago" %((today - afd).days))
    afd = afd.replace(year = today.year + 1)

time_to_afd = afd - today
print("it's just,", time_to_afd.days, "days until April fool's day!")
