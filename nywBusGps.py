#!/usr/bin/env python

import sys
import urllib,urllib2,httplib
import datetime

class nywBusPos:
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
        self.base_url="""services.saucontds.com/tds-map/nyw/nywvehiclePositions.do"""

    def queryBusPosition(self):
        current_time='%d' % ((datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()*1000)
        params=urllib.urlencode({'id':self.node_id,
                                 'time':current_time})
        print current_time
        print params
        print self.base_url

        # req=urllib2.Request(self.base_url,params)
        # print req
        # try:
        #     response=urllib2.urlopen(req)
        #     print response.readlines()
        # except Exception as e:
        #     print 'error open url with error'
        #     print e
        header={"User-Agent":"akahm",
                "Content-type":"application/x-www-form-urlencoded",
                "Accept":"application/json"}
        #conn=httplib.HTTPSConnection(self.base_url)
        #conn.request("GET","",params,header)
        conn=httplib.HTTPSConnection("services.saucontds.com/tds-map/nyw/routemapc.htm?id=33")
        conn.request("GET","")
        try:
            response=conn.getresponse()
            print response.read()
        except Exception as e:
            print "error when get http"
            print e
        # print response
        # print response.read()
        # conn.close()
        # # req=urllib2.Request(self.base_url,params)
        # # response=urllib2.urlopen(req).readlines()
        # print response

    def calcGPSCoord(self,bus_x,bus_y):
        if self.node_id in gps_calc_map:
            gps_x=(bus_x-0.5)*gps_calc_map(self.node_id)("kx")+gps_calc_map(self.node_id)("dx")
            gps_y=(bus_y-0.5)*gps_calc_map(self.node_id)("ky")+gps_calc_map(self.node_id)("dy")
            return [gps_x,gps_y]
        else:
            print "node_id:"+str(self.node_id)+' not existed!'
            return
    

if __name__=="__main__":
    if len(sys.argv)!=2:
        print 'should be:\n'+sys.argv[0]+' <route node id>'
        sys.exit(1)
    route1=nywBusPos(33)
    route1.queryBusPosition()
