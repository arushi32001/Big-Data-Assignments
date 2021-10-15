#!/usr/bin/env python3

# import sys because we need to read and write data to STDIN and STDOUT
import sys
import json
import math
import datetime
# reading entire line from STDIN (standard input) open(stdin, 'r')

desc = ['lane blocked', 'shoulder blocked', 'overturned vehicle']
weather = ['Heavy Snow', 'Thunderstorm', 'Heavy Rain', 'Heavy Rain Showers', 'Blowing Dust']

for i in sys.stdin:
    i = json.loads(i)
    try:
        if type(i['Description']) == str and type(i['Sunrise_Sunset']) == str and math.isnan(i['Severity']) is False and math.isnan(i['Visibility(mi)']) is False and math.isnan(i['Precipitation(in)']) is False and type(i['Weather_Condition']) == str:
            desc_bool = any(description.lower() in i['Description'].lower() for description in desc)
            if desc_bool and i['Severity'] >= 2 and i['Sunrise_Sunset'].lower() == 'night' and i['Visibility(mi)'] <= 10 and i['Precipitation(in)'] >= 0.2 and i['Weather_Condition'] in weather:
                date_time = datetime.datetime.strptime(str(i['Start_Time'])[:19], '%Y-%m-%d %H:%M:%S')
                hour = str(date_time.hour).zfill(2)
                print('%s\t%s\t%s' %(hour, date_time.hour, 1))
    except Exception as e:
    	print(e) 
