import datetime

# 11/30/18 - 11:08am
some_date = datetime.datetime(\
    year=2018, \
    month=11, \
    day=30, \
    hour=11, \
    minute=8, \
    second=55, \
    microsecond=55 \
)

print(some_date)

# some_date.replace(second=0, microsecond=0)
# the above won't work because datetime.replace will return a copy
some_date = some_date.replace(second=0, microsecond=0)

print(some_date)


# Return the day of the week as an integer, where Monday is 0 and Sunday is 6
day_num = datetime.datetime.now().weekday()

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("Today is " + weekday_names[day_num])


