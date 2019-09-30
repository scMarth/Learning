import datetime, pytz

add_date_ts = 1519251780
last_action_ts = 1527176340
close_date_ts = 1519326000

print(add_date_ts)

def print_timestamp(dt):
    # print(dt.strftime('%m/%d/%Y %H:%M %p'))
    # print(dt.strftime('%m/%d/%Y %I:%M %p')) # 12-hour with leading 0
    # print(dt.strftime('%m/%d/%Y %-I:%M %p')) # This doesn't work in Windows apparently

    time_string = dt.strftime('%m').lstrip('0') + '/' + dt.strftime('%d').lstrip('0') + dt.strftime('/%Y ') + dt.strftime('%I').lstrip('0') + dt.strftime(':%M %p')
    print(time_string)

print('Add Date:')
add_date = datetime.datetime.fromtimestamp(add_date_ts)
print_timestamp(add_date)
print('')

print('Last Action:')
last_action = datetime.datetime.fromtimestamp(last_action_ts)
print_timestamp(last_action)
print('')

print('Close Date:')
close_date = datetime.datetime.fromtimestamp(close_date_ts)
print_timestamp(close_date)

'''

Notes: fromtimestamp already converts to local timezone

strftime codes: https://www.programiz.com/python-programming/datetime/strftime

'''