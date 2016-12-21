//  Copyright © 2016 Oh Jun Kwon. All rights reserved.


import json
import urllib.parse
import urllib.request

#APIKEY = 'asd'
APIKEY = '2uZmZ4sisDol7IUPKfnkFctpeV8SgCQ8'


DIRECTION_BASE_URL = 'http://www.mapquestapi.com/directions/v2'
ELEVATION_BASE_URL = 'http://open.mapquestapi.com/elevation/v1'
DIRECTION_SEARCH_URL = '/route'
ELEVATION_SEARCH_URL = '/profile'


def direction_search_url (count, locations):
    'builds and returns URL for direction search'
    query_parameters = [
        ('key', APIKEY), ('from', locations[0]),]

    for i in range(1, count):
        query_parameters.append(('to', locations[i]))

    return DIRECTION_BASE_URL+DIRECTION_SEARCH_URL+'?'+urllib.parse.urlencode(query_parameters)



def get_result(url):
    'takes URL and returns parsed JSON response'
    response = None
    try:
        response = urllib.request.urlopen(url)            
        json_text = response.read().decode(encoding = 'utf-8')      
        return json.loads(json_text)
              
    finally:        
        if response!=None:
            response.close()


def direction_search(count, locations):
    'combining to get search url and json results for directions'
    url = direction_search_url(count, locations)
    return get_result(url)


def elevation_search_url(elev_list):
    'builds and returns URL for elevation search'
    query_parameters = [
        ('key', APIKEY), ('latLngCollection', elev_list)]

    return ELEVATION_BASE_URL+ELEVATION_SEARCH_URL+'?'+urllib.parse.urlencode(query_parameters)


def elevation_search(elev_list, count):
    'combining to get search url and json results for elevation'
    url_list=[]
    json_list =[]

    for i in range(count):
        a = elev_list[i]
        b=','.join(a)

        url = elevation_search_url(b)
        url_list.append(url)

        z=get_result(url_list[i])
        json_list.append(z)


    return json_list


