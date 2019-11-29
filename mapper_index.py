#!/usr/bin/python

# Format of each line is:


import sys

specials = """,.!?:;"()'<>[]#$=-/"""
print(len(specials))
trans = specials.maketrans(specials, ' '*len(specials))

for line in sys.stdin:
    data = line.split("\t")
    
    if len(data) == 19: 
        nodeID, body = data[0], data[4]
        words = body.translate(trans).strip().split()
        nodeID = nodeID.translate(trans).strip()

        for word in words:
            #print "{}/t{}".format(word.lower(),nodeID)
            print (f"{word.lower()}\t{nodeID}")