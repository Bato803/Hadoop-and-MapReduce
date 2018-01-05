#!/usr/bin/python

import sys

phase = "http://www.the-associates.co.uk"
for line in sys.stdin:
    data = line.strip().split()
    
    if len(data)==10:
        ip, identity, username, datetime, timezone, method, path, proto, status, size = data
        # print path
        if(phase in path):
            path = path.replace(phase, "")
        print path
    #print "{0}\t{1}".format(path,1)




    



            
