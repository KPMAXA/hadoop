#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
count = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the weekday name, val is the sale amount


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        #print(f"{oldKey}\t{salesTotal/count}")
        print "{0}\t{1}".format(oldKey,salesTotal/count)
        oldKey = thisKey
        salesTotal = 0
        count = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count += 1

if oldKey is not None:
    #print(f"{oldKey}\t{salesTotal}")
    print "{0}\t{1}".format(oldKey,salesTotal/count)

#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    for line in sys.stdin:
        
        # YOUR CODE HERE