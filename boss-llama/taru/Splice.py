# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:36:54 2017

@author: tarusaraswat
"""

import json
import csv
import time
import datetime
import sys

def isOpen(file, businessID, start, threshold):
    min_Diff =  datetime.timedelta(10000)
    f = open(file, 'r')
    data = json.load(f)
    f.close()
    count = 0
    exceed = 0
    for entry in data:
        if entry['business_id']==businessID:
            count+=1
            print(entry['date'])
            diff = (datetime.datetime.strptime(start, "%Y-%m-%d"))-(datetime.datetime.strptime(entry['date'], "%Y-%m-%d"))
            if(diff < datetime.timedelta(0)):
                exceed += 1
                #print(entry['date'])
            if(diff >= datetime.timedelta(0) and diff <= min_Diff):
                min_Diff = diff
    print(count)
    #print(exceed)
    #print(min_Diff)
    #print(datetime.timedelta(threshold))
    if exceed > 0:
        if min_Diff < datetime.timedelta(10000):
            return True
        else:
            return False
    if(min_Diff <= datetime.timedelta(threshold)):
        return False
    else:
        return True
    #filteredList = [x for x in data if x['business_id']==businessID and (datetime.datetime.strptime(start, "%Y-%m-%d"))-(datetime.datetime.strptime(x['date'], "%Y-%m-%d")) <= datetime.timedelta(threshold) ]
    #return filteredList
    
'''To take a splice of data belonging to a period'''
def splice(file, businessID, start, end):
    f = open(file, 'r')
    data = json.load(f)
    f.close()
    start_stmp = time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d").timetuple())
    end_stmp = time.mktime(datetime.datetime.strptime(end, "%Y-%m-%d").timetuple())
    output_dict = [x for x in data if x['business_id']==businessID and (time.mktime(datetime.datetime.strptime(x['date'], "%Y-%m-%d").timetuple())) >= start_stmp and (time.mktime(datetime.datetime.strptime(x['date'], "%Y-%m-%d").timetuple())) <= end_stmp ]
    return (output_dict)
    
#print(isOpen('yelp_academic_dataset_review_1.json',"4P-vTvE6cncJyUyLh73pxw", "2011-02-01", 0 ))
print(splice('yelp_academic_dataset_review_1.json',"4P-vTvE6cncJyUyLh73pxw", "2011-02-01", "2016-02-01" ))