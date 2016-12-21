//  Copyright © 2016 Oh Jun Kwon. All rights reserved.

import interact
import implement


def mapquest():

    count = num_location()
    locations = take_location(count)
    count1 = num_output()
    outputs = take_output(count1)

    try:
        result = interact.direction_search(count, locations)
        implement.determine_output(outputs, result, count)

        credit()
    except:
        print('\nMAPQUEST ERROR')
        




def num_location():
    'takes number of locations the trip will consist of'
    num = int(input())
    return num

def take_location(count):
    'take input of described location per line'
    locations=[]
    for i in range(count):
        
        query = input()
        locations.append(query)

    return locations
        

def num_output():
    'takes number of outputs desired'
    num = int(input())
    return num

def take_output(count1):
    'takes input of description of output per line'
    outputs = []
    for i in range(count1):
        query = input()
        outputs.append(query)

    return outputs


def credit():
    'give courtesy to the database'
    print('\nDirections Courtesy of MapQuest; '
          'Map Data Copyright OpenStreetMap Contributors\n')

def ourNames() :
    'return who worked on this project as the instruction states to do'
    return ((27062056, "Oh Jun Kwon"))


if __name__ == '__main__':
    mapquest()
