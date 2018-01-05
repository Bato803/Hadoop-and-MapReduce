#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

next(reader)

for line in reader:
    
    if len(line)==19:
        node_id = line[0]
        body = line[4]
        words = re.findall(r"[a-zA-Z]+", body)
        words = [word.lower() for word in words]

        for word in words:
            print "{0}\t{1}".format(word, node_id)


