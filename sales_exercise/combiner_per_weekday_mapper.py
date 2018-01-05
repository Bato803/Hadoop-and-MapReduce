#!/usr/bin/python

"""
Count the average of sales per weekday
with combiner
"""




import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip().split('\t')
    
    if(len(line)!=6):
        continue

    date = line[0]
    year, month, day = (int(x) for x in date.split('-'))
    dt = datetime(year, month, day)

    week_day = dt.weekday()

    print "{0}\t{1}".format(week_day, line[4])

