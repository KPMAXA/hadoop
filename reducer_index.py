#!/usr/bin/python

import sys

nodeList= []
oldKey = None

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, thisNode = data_mapped

    if oldKey and oldKey != thisWord:
        nodeList.sort()
        print(f"{oldKey}\t{nodeList}")
        #print "{0}\t{1}".format(oldKey,nodeList)
        oldKey = thisWord
        nodeList = []

    oldKey = thisWord
    nodeList.append(thisNode)

if oldKey is not None:
    nodeList.sort()
    print(f"{oldKey}\t{nodeList}")
    #print "{0}\t{1}".format(oldKey,nodeList)
