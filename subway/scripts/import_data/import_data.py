from subway.models import *

import csv
import sys

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        date = row[1]
        dest = row[0]
        duration = row[2]
        depart = row[6]
        arrive = row[7]
        t0 = row[3]
        t1 = row[4]
        t2 = row[5]

        if t0 != None:
            if Train.objects.filter(symbol=t0).exists():
                train_0 = Train.objects.get(symbol=t0)
            elif t0 == '':
                train_0 = None
            else:
                train_0 = Train(symbol=t0)
                train_0.save()

        if t1 != None:
            if Train.objects.filter(symbol=t1).exists():
                train_1 = Train.objects.get(symbol=t1)
            elif t1 == '':
                train_1 = None
            else:
                train_1 = Train(symbol=t1)
                train_1.save()

        if t2 != None:
            if Train.objects.filter(symbol=t2).exists():
                train_2 = Train.objects.get(symbol=t2)
            elif t2 == '':
                train_2 = None
            else:
                train_2 = Train(symbol=t2)
                train_2.save()

        if dest != None:
            if Destination.objects.filter(name=dest).exists():
                destination = Destination.objects.get(name=dest)
            else:
                destination = Destination(name=dest)
                destination.save()

        if not Trip.objects.filter(date=date, destination=destination).exists():
            trip = Trip(
                destination=destination,
                date=date,
                arrival=arrive,
                departure=depart,
                duration=duration,
                train_0=train_0,
                train_1=train_1,
                train_2=train_2
            )
            trip.save()
        else:
            trip = Trip.objects.get(date=date, destination=destination)
            trip.arrival = arrive
            trip.departure = depart
            trip.duration = duration
            trip.train_0 = train_0 
            trip.train_1 = train_1 
            trip.train_2 = train_2