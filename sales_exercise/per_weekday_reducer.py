"""

Compute the average sales per weekday. 

"""




#!/usr/bin/python

import sys
import collections

count_cost = collections.defaultdict(float)
count_day = collections.defaultdict(int)

for line in sys.stdin:
    data = line.strip().split('\t')

    if(len(data)!=2):
        continue

    day, cost = data
    
    count_cost[day] += float(cost)
    count_day[day] += 1

for key in count_cost:
    print "{0}\t{1}".format(key, count_cost[key]/count_day[key])


