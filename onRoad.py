#!/usr/bin/env python

# onRoad class take 2d array [[lat1,lng1],[lat2,lng2]...] and output nearest on road lat,lng points pairs
# this class is completely depend on Google Road API

# Hao Men
# 2016/07/23

import sys
import urllib,urllib2,httplib
import json

class onRoad():
    def __init__(self):
        self.google_api_key="AIzaSyBdI6UofUML6LnfnWHTxexprc9uD5u4UCY"
        self.base_url="roads.googleapis.com"
        self.second_url="/v1/nearestRoads"

    def getRoadPositions(self, raw_gps_list):
        gps_input=''
        for gps_point in raw_gps_list[:-1]:
            gps_input+=str(format(gps_point[0],'.5f'))+','+str(format(gps_point[1],'.5f'))+'|'
        gps_input+=str(gps_point[0])+','+str(gps_point[1])
        params=urllib.urlencode({'points':gps_input,
                                 'key':self.google_api_key})
        path=self.second_url+"?"+params
        #print 'path=:'
        #print path
        conn=httplib.HTTPSConnection(self.base_url,443)
        conn.request("GET",path)
        try:
            response=conn.getresponse()
            pos_list=response.read()
            #print pos_list
            pos_json=json.loads(pos_list)["snappedPoints"]
            pos_dict={}
            pos_val=[]
            for item in pos_json:
                if item["originalIndex"] in pos_dict.keys():
                    pass
                else:
                    pos_dict[item["originalIndex"]]=0
                    #print item
                    p=[item["location"]["latitude"],item["location"]["longitude"]]
                    #print p
                    pos_val.append(p)
            if len(pos_val)!=len(raw_gps_list):
                print "onRoad:: Google Map API error, input gps point didnt get same amount of on road points!"
                return None
            else:
                return pos_val
        except Exception as e:
            print e

if __name__=="__main__":
    raw_gps=[[40.75456,-73.98288],[40.75988,-73.9816],[40.75932,-73.97974]]
    a_road=onRoad()
    print raw_gps
    new_gps=a_road.getRoadPositions(raw_gps)
    print new_gps
