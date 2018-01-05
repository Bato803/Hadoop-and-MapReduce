# Count how many sales for each store - mapper

import sys

for line in sys.stdin:
    words = line.strip().split("\t")
	
    if len(words)==6:
        data, time, store, item, cost, payment = words
	print "{0} \t {1}".format(item, cost)	
