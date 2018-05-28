from datetime import datetime
import csv 
import sys
import re

file_path = sys.argv[1]
file_name_pattern = re.compile('.*/(.*).csv')
file_name_search = file_name_pattern.search(file_path)
if file_name_search:
    file_name = file_name_search.group(1)
file_name = file_name.replace('.csv','')
processed_trips = []

with open(file_path, 'r') as f:
    reader = csv.reader(f)
    next(reader, None) # skip header
    for row in reader:
        dest = row[0].strip()
        date = row[1].strip()
        duration = row[2].strip()
        train_0 = row[3].strip()
        train_1 = row[4].strip()
        train_2 = row[5].strip()
        depart = row[6].strip()
        arrive = row[7].strip()

        date = datetime.strptime(date, "%m/%d/%y")
        date = date.strftime("%Y-%m-%d")

        processed_trips.append([
            dest,
            date,
            duration,
            train_0,
            train_1,
            train_2,
            depart,
            arrive
        ])

with open("./{}-processed.csv".format(file_name), 'w') as fout:
    writer = csv.writer(fout)
    writer.writerows(processed_trips)



