import datetime

start_time = datetime.datetime.now()

def get_date_string():
    return "{}-{}-{}".format(
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        datetime.datetime.now().year
    )


print(get_date_string())

for i in range(10000):
    continue

end_time = datetime.datetime.now()

print("{}".format(end_time - start_time))