//  Copyright © 2016 Oh Jun Kwon. All rights reserved.

import interact


APIKEY = '2uZmZ4sisDol7IUPKfnkFctpeV8SgCQ8'

class Step:
    def __init__(self):
        pass
    
    def step(self, result):
        'pick steps from json result'
        x = result['route']['legs']
        print("\nDIRECTIONS")
        for item in x:
            for item1 in item['maneuvers']:
                print(item1['narrative'])
                

class Totaldistance:
    def __init__(self):
        pass

    def totaldistance(self, result):
        'pick totaldistance from json result'
        total_distance = result['route']['distance']   
        print('\nTOTAL DISTANCE: {} miles'.format(int(round(total_distance,0))))


class Totaltime:
    def __init__(self):
        pass

    def totaltime(self, result):
        'pick totaltime from json result'
        total_time = result['route']['time']
        print("\nTOTAL TIME: {} minutes".format(int(round(total_time/60,0))))


class Latlong:
    def __init__(self):
        pass

    def latlong(self, result):
        'pick latlong from json result'
        
        position = result['route']['locations']
        
        print("\nLATLONG")
        for element in position:
            
            lng=element['latLng']['lng']
            lat=element['latLng']['lat']
            lng=round(lng,2)
            lat=round(lat,2)

            if lat<0:
                lat=(str(lat).replace("-","")) + "S"    
            elif lat>=0:
                lat=str(lat) + "N"
            if lng<0:
                lng=(str(lng).replace("-","")) + "W"
            elif lng>=0:
                lng=str(lng) + "E"
        
            print(lat, lng)


class Elevation:
    def __init__(self):
        pass

    def get_elevation(self, result):
        'get latlong from direction url and returns it'
        elev_list=[]
        position = result['route']['locations']
        for element in position:
            lat = (element['latLng']['lat'])
            lng = (element['latLng']['lng'])

            elev_list.append([str(lat),str(lng)])

        return elev_list

        
    def show_elevation(self, elevation, count):
        'get elevation from elevation url json result'
        print("\nELEVATIONS")
        
        for i in range(count):
            a=(elevation[i]['elevationProfile'][0]['height'])
            print(round(a*3.28084))





def determine_output(list_output, result, count):
    s = Step()
    td = Totaldistance()
    tt = Totaltime()
    ll = Latlong()
    e = Elevation()

    try:
        for item in list_output:
            if item.upper() == "STEPS":
                s.step(result)

            elif item.upper() == "TOTALDISTANCE":
                td.totaldistance(result)

            elif item.upper() == "TOTALTIME":
                tt.totaltime(result)
            
            elif item.upper() == "LATLONG":
                ll.latlong(result)

            elif item.upper() == 'ELEVATION':      
                elev_list = e.get_elevation(result)
                elevation = interact.elevation_search(elev_list, count)
                e.show_elevation(elevation, count)

    except:
        print('\nNO ROUTE FOUND')
    




    
    
            
