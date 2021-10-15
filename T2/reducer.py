#!/usr/bin/env python3
from operator import itemgetter
import sys

current_state = None
current_city = None
state_count = 0
city_count = 0

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    state_city, count = line.split('\t', 1)
    state, city = state_city.split('#', 1)
    printed = False

    # splitting the data on the basis of tab we have provided in mapper.py
    try:
        count = int(count)
    except ValueError:
        continue

    # Only works because Hadoop sorts map output by key (here: word) before it is passed to the reducer
    if current_state == state:
        state_count += count
    else:
        if current_city:
            print ('%s\t%s' % (current_city[:-2], city_count))
            printed = True
        if current_state:
            print ('%s\t%s' % (current_state, state_count))

        print('%s' % (state))
        state_count = count
        current_state = state

    if current_city == city:
        city_count += count
    else:
        #if current_city and printed == False:
        if current_city and printed == False:
            print ('%s\t%s' % (current_city[:-2], city_count))

        city_count = count
        current_city = city


#if current_state == state is False:
print('%s\t%s' % (current_city[:-2], city_count))
print('%s\t%s' % (current_state, state_count))
