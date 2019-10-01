import datetime, pytz

timestamps = [
    [1557216840, 1559075400],
    [1557217740, 1557961200],
    [1557219000, 1558126980]
]

def print_timestamp(dt):
    # print(dt.strftime('%m/%d/%Y %H:%M %p'))
    # print(dt.strftime('%m/%d/%Y %I:%M %p')) # 12-hour with leading 0
    # print(dt.strftime('%m/%d/%Y %-I:%M %p')) # This doesn't work in Windows apparently

    time_string = dt.strftime('%m').lstrip('0') + '/' + dt.strftime('%d').lstrip('0') \
        + dt.strftime('/%Y ') + dt.strftime('%I').lstrip('0') + dt.strftime(':%M %p')
    print(time_string)

for timestamp in timestamps:
    add_date_ts, last_action_ts = timestamp
    add_date_dt = datetime.datetime.fromtimestamp(add_date_ts)
    last_action_dt = datetime.datetime.fromtimestamp(last_action_ts)
    print('Add Date:')
    print_timestamp(add_date_dt)
    print('Last Action:')
    print_timestamp(last_action_dt)
    print('')

'''

Notes: fromtimestamp already converts to local timezone

strftime codes: https://www.programiz.com/python-programming/datetime/strftime

'''