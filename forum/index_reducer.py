#!/usr/bin/python

import sys
import collections 

index = collections.defaultdict(list)

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data)!=2:
        continue

    word, id = data

    index[word].append(id)


for word in index:
    if word=='fantastic' or word == 'fantastically':
        print "{0}\t{1}\t{2}\n".format(word, len(index[word]), index[word])
    
