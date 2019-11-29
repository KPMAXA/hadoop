#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
#%h %l %u %t \"%r\" %>s %b
#pip install apache-log-parser==1.7.0

import sys
import apache_log_parser

for line in sys.stdin:
    data = line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b")
    #if len(data) == 6:
        #date, time, store, item, cost, payment = data
        #print '{0}\t{1}'.format(store,cost)
        #print(f"{store}\t{cost}")
