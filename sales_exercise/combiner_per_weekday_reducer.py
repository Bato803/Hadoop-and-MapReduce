#!/usr/bin/python

"""

Compute the average sales per weekday with combiner

"""





import sys
import collections

count_cost = collections.defaultdict(float)

for line in sys.stdin:
    data = line.strip().split('\t')

    if(len(data)!=2):
        continue

    day, cost = data
    
    count_cost[day] += float(cost)

for key in count_cost:
    print "{0}\t{1}".format(key, count_cost[key])


