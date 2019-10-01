import datetime, pytz

timestamps = [
    1556550720,
    1556293200,
    1558365180
]

def print_timestamp(dt):
    # print(dt.strftime('%m/%d/%Y %H:%M %p'))
    # print(dt.strftime('%m/%d/%Y %I:%M %p')) # 12-hour with leading 0
    # print(dt.strftime('%m/%d/%Y %-I:%M %p')) # This doesn't work in Windows apparently

    time_string = dt.strftime('%m').lstrip('0') + '/' + dt.strftime('%d').lstrip('0') \
        + dt.strftime('/%Y ') + dt.strftime('%I').lstrip('0') + dt.strftime(':%M %p')
    print(time_string)

for timestamp in timestamps:
    dt = datetime.datetime.fromtimestamp(timestamp)
    print_timestamp(dt)
    print('')

'''

Notes: fromtimestamp already converts to local timezone

strftime codes: https://www.programiz.com/python-programming/datetime/strftime

'''