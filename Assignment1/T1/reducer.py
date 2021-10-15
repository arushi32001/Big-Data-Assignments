#!/usr/bin/env python3

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    _, word, count = line.split('\t', 2)
    # splitting the data on the basis of tab we have provided in mapper.py
    try:
        count = int(count)
    except ValueError:
        continue

    # Only works because Hadoop sorts map output by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# output the last word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
