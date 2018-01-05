#!/usr/bin/python

import sys

num_Sales = 0
val_Sales = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    #if oldKey and oldKey != thisKey:
    #    print oldKey, "\t", maxVal
    #    oldKey = thisKey;
    #    maxVal = 0

    #oldKey = thisKey
    #maxVal = max(maxVal, float(thisSale)) 
    num_Sales += 1
    val_Sales += float(thisSale)


#if oldKey != None:
print "Total number of sales {0}, total value is {1}".format(num_Sales, val_Sales)

