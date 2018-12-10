import datetime

# parameter examples:
#    time = '13:01'
#    date = '2/12/2013'
def to_datetime(time, date):
    # at the very least, we need a time
    if time is None:
        return None

    result = datetime.datetime.now()

    hour, minute = time.split(":")
    result = result.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)

    if date is not None:
        month, day, year = date.split("/")
        result = result.replace(month=int(month), day=int(day), year=int(year))

    return result

def get_day_string_from_day_num(day_num):
    hashmap = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday"
    }

    return hashmap[day_num]

holidays_2019 = [
    "1/1/2019",
    "1/21/2019",
    "2/12/2019",
    "2/18/2019",
    "5/27/2019",
    "7/4/2019",
    "9/2/2019",
    "11/11/2019",
    "11/28/2019",
    "11/29/2019",
    "12/24/2019",
    "12/25/2019"
]

holidays_2019_dts = []

for date_str in holidays_2019:
    dt = to_datetime("12:00", date_str)
    holidays_2019_dts.append(dt)

curr_day = to_datetime("12:00", "1/1/2019")
one_day = datetime.timedelta(days=1)

curr_week_type = 1 # 1 for week 1 ; 2 for week 2

'''
store datetimes ; year_days[1][0] = days that are week 1, Mondays
'''
year_days = {
    1 : {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : [],
    },
    2 : {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : [],
    }
}

while curr_day.year == 2019:
    if curr_day not in holidays_2019_dts:
        weekday = curr_day.weekday()
        if weekday in range(0,5):
            year_days[curr_week_type][weekday].append(curr_day)

    # switch week type after every sunday
    if curr_day.weekday() == 6:
        curr_week_type = 2 if curr_week_type is 1 else 1

    curr_day = curr_day + one_day

for week in [1, 2]:
    for day in range(0,5):
        dts = year_days[week][day]

        print("Week {0} : {1}:".format(week, get_day_string_from_day_num(day)))
        for dt in dts:
            month = dt.strftime("%B")
            day = dt.day
            print("\t{0}, {1}".format(month, day))
        print("")