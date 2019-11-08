import datetime

timestamps = [
    1519251840,
    1527176940,
    1519325940
]

def print_timestamp(ts):
    # print(dt.strftime('%m/%d/%Y %H:%M %p'))
    # print(dt.strftime('%m/%d/%Y %I:%M %p')) # 12-hour with leading 0
    # print(dt.strftime('%m/%d/%Y %-I:%M %p')) # This doesn't work in Windows apparently

    dt = datetime.datetime.fromtimestamp(ts)

    time_string = dt.strftime('%m').lstrip('0') + '/' + dt.strftime('%d').lstrip('0') \
        + dt.strftime('/%Y ') + dt.strftime('%I').lstrip('0') + dt.strftime(':%M %p')
    print(time_string)

for timestamp in timestamps:
    print_timestamp(timestamp)