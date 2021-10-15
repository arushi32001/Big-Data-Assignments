#!/usr/bin/env python3

# import sys because we need to read and write data to STDIN and STDOUT
import sys
import json
import math
import requests

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
D = float(sys.argv[3])
def euclidean_dist(latitude1, longitude1, latitude2, longitude2):
    dist = math.sqrt(pow((latitude2 - latitude1), 2) + pow((longitude2 - longitude1), 2))
    return dist

# reading entire line from STDIN (standard input) open(stdin, 'r')


for i in sys.stdin:
    i = json.loads(i)
    try:
        if math.isnan(i['Start_Lat']) == False and math.isnan(i['Start_Lng']) == False:
            dist = euclidean_dist(i['Start_Lat'], i['Start_Lng'], latitude, longitude)
            if dist <= D:
                data1 = {"latitude": i['Start_Lat'], "longitude": i['Start_Lng']}
                res = requests.post('http://20.185.44.219:5000/',json = data1)
                city, state = res.json()['city'], res.json()['state']
                if type(city) == str and type(state) == str:
                    state_city = state + '#' + city + ' ~'
                    print('%s\t%s' %(state_city, 1))
    except Exception as e:
        print(e)
