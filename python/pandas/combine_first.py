import pandas as pd

# create sample dataframes
one = pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'value': [10, 20], 'other_value': [100, 200], 'third_value': [None, None]})
two = pd.DataFrame({'date': ['2022-01-02', '2022-01-03'], 'value': [30, 40], 'other_value': [None, 400], 'third_value': [99, 99]})

print(one)
print('')
print(two)
print('')

# set 'date' as the index for both dataframes
one.set_index('date', inplace=True)
two.set_index('date', inplace=True)

# combine the dataframes and overwrite values in 'one' with values from 'two'
one = two.combine_first(one)

# reset index to make 'date' a column again
one.reset_index(inplace=True)

# print the resulting dataframe
print(one)




print('')

from datetime import date, timedelta

# get yesterday's date to use as input for historical API
today = date.today()
yesterday = today - timedelta(days=1)
print(today.strftime("%#m/%#d/%Y"))