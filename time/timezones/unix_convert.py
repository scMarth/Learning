import datetime

ts = 1519323540 # seconds since the Epoch
d = datetime.datetime.fromtimestamp(ts)
print(str(d)) # prints "2018-02-22 10:19:00"