import sys
import datetime


'''
given a datetime, return which quarter of the day it is

return values:

12am - 6am - returns 1
6am - 12pm - returns 2
12pm - 6pm - returns 3
6pm - 12am - returns 4

'''
def get_period_quarter_number(input_date):
    if input_date.hour >= 0 and input_date.hour < 6:
        return 1
    elif input_date.hour == 6:
        return 2
    elif input_date.hour > 6 and input_date.hour < 12:
        return 2
    elif input_date.hour == 12:
        return 3
    elif input_date.hour > 12 and input_date.hour < 18:
        return 3
    elif input_date.hour == 18:
        return 4
    else: # input_date.hour > 18:
        return 4

# given two datetime.datetimes, returns an array containing two results
# the first is the leakage estimate in gallons, and the second is the
# total duration in minutes
def estimate_leakage_with_dts(start_date, end_date, addr_count):
    # multipliers for Average Flow Rates per EDU 
    multipliers = { \
        1 : 0.2, \
        2 : 0.15, \
        3 : 0.13, \
        4 : 0.03 \
    }

    #set average people per housing unit
    # perunit = 3.67

    # exit if the start date is later than the end date
    if start_date > end_date:
        sys.stderr.write("Error in estimate_leakage: start date is later than the end date. Aborting")
        sys.exit()

    # if both times are the same
    if start_date == end_date:
        return 0

    one_minute = datetime.timedelta(minutes=1)

    # a mapping from period quarter number to how many minutes have been
    # spent in that time period
    minutes_in_period_qarters = { \
        1 : 0, \
        2 : 0, \
        3 : 0, \
        4 : 0 \
    }

    # find out how many minutes per quarter of day
    duration_in_minutes = 0
    current_date = start_date
    while current_date < end_date:
        current_quarter = get_period_quarter_number(current_date)
        minutes_in_period_qarters[current_quarter] += 1
        duration_in_minutes += 1
        current_date = current_date + one_minute

    # find the total leakage in gallons
    leakage = 0
    for quarter_number in minutes_in_period_qarters:
        # leakage += perunit * addrCount * minutes_in_period_qarters[quarter_number] * multipliers[quarter_number]
        leakage += addr_count * minutes_in_period_qarters[quarter_number] * multipliers[quarter_number]

    return [leakage, duration_in_minutes]

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

def get_leakage_estimates(start_time, start_date, end_time, end_date, addr_count):
    dt_start = to_datetime(start_time, start_date)
    dt_end = to_datetime(end_time, end_date)
    return estimate_leakage_with_dts(dt_start, dt_end, addr_count)

# example of how to call function
result = get_leakage_estimates(start_time="11:08", start_date="11/30/2018", end_time="14:08", end_date="012/15/2018", addr_count=1)
print("Estimated leakage (gallons): " + str(result[0]))
print("Duration of leakage (minutes): " + str(result[1]))