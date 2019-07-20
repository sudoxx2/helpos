import pandas as pd
from datetime import timedelta
import datetime
import numpy as np

# prep data for dataframe
lst = {'call_start_time':['7/28/2015','8/10/2015','7/28/2015','7/28/2015'],
        'level':['1','0','1','1'],
        'id':['66547', '66272', '66547','66547']}

# create dataframe
df = pd.DataFrame(lst)

# convert to TimeDelta object to subtract days
for index, row in df.iterrows():
    row['call_start_time'] = datetime.datetime.strptime(row['call_start_time'], "%m/%d/%Y").date()

# get the end date by adding 20 days to start day
df["end_of_20_days"] = df["call_start_time"] + timedelta(days=20)

# used below comment for testing might need it later
# df['Difference'] = (df['end_of_20_days'] - df['call_start_time']).dt.days

# created person class to keep track of days_count and id
class Person(object):
    def __init__(self, id, start_date, end_date):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.days_count = 1

# create list to hold objects of person class
person_list = []

# populate person_list with Person objects and their attributes
for index, row in df.iterrows():
    # get result_id to use as conditional for populating Person objects
    result_id = any(x.id == row['id'] for x in person_list)

    # initialize Person objects and inject with data from dataframe
    if len(person_list) == 0:
        person_list.append(Person(row['id'], row['call_start_time'], row['end_of_20_days']))
    elif not(result_id):
        person_list.append(Person(row['id'], row['call_start_time'], row['end_of_20_days']))
    else:
        for x in person_list:
            # if call_start_time is within 20 days time frame, increment day_count to Person object
            diff = (x.end_date - row['call_start_time']).days
            if x.id == row['id'] and diff <= 20 :
                x.days_count += 1
                break

# flag to check if nobody hit the sales mark
flag = 0

# print out only person_list ids who have hit the sales mark
for person in person_list:
    if person.days_count >= 10:
        flag = 1
        print("person id:{} has made {} calls within the past 20 days since first call date".format(person.id, person.days_count))

if flag == 0:
    print("No one has hit the sales mark")

