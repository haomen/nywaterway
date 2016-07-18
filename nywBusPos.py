#!/usr/bin/env python

import sys
import urllib,urllib2,httplib
import datetime
import json

class nywBusPos(object):
    gps_calc_map={
        33:{
            "kx":5.32196e-5,
            "dx":-74.007868,
            "ky":-4.03097e-5,
            "dy":40.774535
        }
    }

    def __init__(self, node_id):
        self.node_id=node_id
        #set up http handle
        self.base_url="services.saucontds.com"
        self.secnd_url="/tds-map/nyw/nywvehiclePositions.do"
    def queryBusPosition(self):
        current_time='%d' % ((datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()*1000)
        params=urllib.urlencode({'id':self.node_id,
                                 'time':current_time})
        path=self.secnd_url+"?"+params

        # comment header in case we will use it in the future
        # header={"User-Agent":"akahm",
        #         "Content-type":"application/x-www-form-urlencoded",
        #         "Accept":"application/json"}

        conn=httplib.HTTPSConnection(self.base_url,443)
        conn.request("GET",path)
        try:
            response=conn.getresponse()
            pos_list=response.read()
            return json.loads(pos_list)
        except Exception as e:
            print "error when get http"
            print e

    def calcGPSCoord(self,bus_x,bus_y):
        if self.node_id in self.gps_calc_map:
            gps_x=(bus_x-0.5)*self.gps_calc_map[self.node_id]["kx"]+self.gps_calc_map[self.node_id]["dx"]
            gps_y=(bus_y-0.5)*self.gps_calc_map[self.node_id]["ky"]+self.gps_calc_map[self.node_id]["dy"]
            return [gps_x,gps_y]
        else:
            print "node_id:"+str(self.node_id)+' not existed!'
            return

    def queryBusGPSPosition(self,internal,pos_list):
        if internal==True:
            pos_list=self.queryBusPosition()

        for pos in pos_list:
            [gps_x,gps_y]=self.calcGPSCoord(pos['x'],pos['y'])
            pos['gps_x']=gps_x
            pos['gps_y']=gps_y
            pos['orientation']=pos['i']
            pos['bus_id']=pos['o']
            pos.pop('x')
            pos.pop('y')
            pos.pop('i')
            pos.pop('o')
        return pos_list

if __name__=="__main__":
    if len(sys.argv)!=2:
        print 'should be:\n'+sys.argv[0]+' <route node id>'
        sys.exit(1)
    route1=nywBusPos(33)

    #get raw output from nywaterway bus location (relative location to their static image coordinate system)
    pos_list=route1.queryBusPosition()
    for pos in pos_list:
        print pos

    #get gps location and orientation of this route
    gps_pos_list=route1.queryBusGPSPosition()
    for pos in gps_pos_list:
        print pos
