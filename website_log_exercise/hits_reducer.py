#!/usr/bin/python

import sys

num_hits = 0
cur_path = None
max_hits = 0
max_hits_name = None

for p in sys.stdin:
    new_path = p.strip().split()
    if len(new_path)!= 1:
        continue
 

    if cur_path and cur_path!=new_path:
        # /assets/js/the-associates.js
        # if cur_path[0] == "/assets/js/the-associates.js":
        # if cur_path[0] == "10.99.99.186":
        #    print "{0}\t{1}".format(cur_path[0],num_hits)
        if num_hits>max_hits:
            max_hits = num_hits
            max_hits_name = cur_path
        
        num_hits = 0

    num_hits += 1 
    cur_path = new_path

if cur_path:
    if num_hits > max_hits:
        max_hits = num_hits
        max_hits_name = cur_path

    print "{0}\t{1}".format(max_hits_name, max_hits)
