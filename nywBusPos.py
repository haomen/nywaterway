#!/usr/bin/env python

import sys
import urllib,urllib2,httplib
import datetime
import json
import onRoad

class nywBusPos(object):
    gps_calc_map={
        1:{
            "kx":4.19561711977e-05,
            "dx":-74.01075934,
            "ky":-3.17827810853e-05,
            "dy":40.7639483191
        },
        21:{
            "kx":4.19561711977e-05,
            "dx":-74.01075934,
            "ky":-3.17827810853e-05,
            "dy":40.7639483191
        },
        22:{
            "kx":5.32196294685e-05,
            "dx":-74.0078684655,
            "ky":-4.03097217025e-05,
            "dy":40.7745351667
        },
        32:{
            "kx":5.32196294685e-05,
            "dx":-74.0078684655,
            "ky":-4.03097217025e-05,
            "dy":40.7745351667
        },
        33:{
            "kx":5.32196294685e-05,
            "dx":-74.0078684655,
            "ky":-4.03097217025e-05,
            "dy":40.7745351667
        },
        34:{
            "kx":5.32196294685e-05,
            "dx":-74.0078684655,
            "ky":-4.03097217025e-05,
            "dy":40.7745351667
        },
        36:{
            "kx":4.19561711977e-05,
            "dx":-74.01075934,
            "ky":-3.17827810853e-05,
            "dy":40.7639483191
        },
        38:{
            "kx":5.32196294685e-05,
            "dx":-74.0078684655,
            "ky":-4.03097217025e-05,
            "dy":40.7745351667
        },
        40:{
            "kx":6.91236284724e-05,
            "dx":-74.024482627,
            "ky":-5.23761429476e-05,
            "dy":40.7615930374
        },
        42:{
            "kx":6.91236284724e-05,
            "dx":-74.024482627,
            "ky":-5.23761429476e-05,
            "dy":40.7615930374
        },
        43:{
            "kx":6.91236284724e-05,
            "dx":-74.024482627,
            "ky":-5.23761429476e-05,
            "dy":40.7615930374
        },
        50:{
            "kx":1.54016195416e-05,
            "dx":-74.0197316823,
            "ky":-1.1639200567e-05,
            "dy":40.7784652027
        },
        51:{
            "kx":3.79140478468e-05,
            "dx":-74.0236841951,
            "ky":-2.8649426405e-05,
            "dy":40.7928313051
        },
        52:{
            "kx":2.23120664492e-05,
            "dx":-74.0132495264,
            "ky":-1.68588297347e-05,
            "dy":40.7915239105
        },
        53:{
            "kx":5.7051447378e-05,
            "dx":-74.0248857047,
            "ky":-4.31020268368e-05,
            "dy":40.8126707301
        },
        54:{
            "kx":3.90662175407e-05,
            "dx":-74.0068704335,
            "ky":-2.80371438772e-05,
            "dy":40.7605671819
        },
        61:{
            "kx":2.92631163844e-05,
            "dx":-74.0313198258,
            "ky":-2.21359215733e-05,
            "dy":40.7788930637
        },
        62:{
            "kx":2.92631163844e-05,
            "dx":-74.0313198258,
            "ky":-2.21359215733e-05,
            "dy":40.7788930637
        },
        70:{
            "kx":5.49065711965e-05,
            "dx":-85.4353773209,
            "ky":-4.18517944577e-05,
            "dy":40.2033832131
        },
        71:{
            "kx":6.22756562791e-05,
            "dx":-85.4499693265,
            "ky":-4.74643563457e-05,
            "dy":40.2115223806
        },
        72:{
            "kx":6.22655584254e-05,
            "dx":-85.4016567291,
            "ky":-4.74643563457e-05,
            "dy":40.2005241692
        },
        73:{
            "kx":6.22722459914e-05,
            "dx":-85.3971109914,
            "ky":-4.74643563457e-05,
            "dy":40.2078086988
        },
        74:{
            "kx":5.07400860111e-05,
            "dx":-85.3985465772,
            "ky":-3.87685444276e-05,
            "dy":40.1944982781
        },
        75:{
            "kx":5.11423707575e-05,
            "dx":-85.3987179505,
            "ky":-3.90759249201e-05,
            "dy":40.1955420542
        },
        76:{
            "kx":6.76219983461e-05,
            "dx":-85.4340251521,
            "ky":-5.16705173396e-05,
            "dy":40.1975820642
        },
        77:{
            "kx":6.76634068068e-05,
            "dx":-85.4156500123,
            "ky":-5.16705173396e-05,
            "dy":40.2390972774
        },
        78:{
            "kx":6.76585329845e-05,
            "dx":-85.4255267934,
            "ky":-5.16705173396e-05,
            "dy":40.2342153759
        },
        79:{
            "kx":6.76567946065e-05,
            "dx":-85.4388159169,
            "ky":-5.16705173396e-05,
            "dy":40.232473827
        },
        80:{
            "kx":6.7623198543e-05,
            "dx":-85.4195870753,
            "ky":-5.16705173396e-05,
            "dy":40.1987865724
        },
        81:{
            "kx":7.03009113414e-05,
            "dx":-85.4449345958,
            "ky":-5.36919779021e-05,
            "dy":40.2308011374
        },
        82:{
            "kx":6.51371824277e-05,
            "dx":-85.4024524169,
            "ky":-4.97456790255e-05,
            "dy":40.232311531
        },
        83:{
            "kx":4.46894925069e-05,
            "dx":-85.3933681924,
            "ky":-3.41296358769e-05,
            "dy":40.2256484674
        },
        84:{
            "kx":4.65259975033e-05,
            "dx":-73.9888984832,
            "ky":-3.51984965511e-05,
            "dy":40.8577162401
        },
        85:{
            "kx":4.03449548021e-05,
            "dx":-73.984421376,
            "ky":-3.05242075395e-05,
            "dy":40.8513368133
        },
        86:{
            "kx":4.68588420913e-05,
            "dx":-73.9971729599,
            "ky":-3.54623914995e-05,
            "dy":40.8352948348
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

    def queryBusGPSPosition(self):
        pos_list=self.queryBusPosition()
        for pos in pos_list:
            [gps_x,gps_y]=self.calcGPSCoord(pos['x'],pos['y'])
            pos['gps_x']=gps_x
            pos['gps_y']=gps_y
            pos['orientation']=pos['i']/5.4
            pos['bus_id']=pos['o']
            pos.pop('x')
            pos.pop('y')
            pos.pop('i')
            pos.pop('o')
        return pos_list

    def queryBusGPSPositionOnRoad(self):
        pos_list=self.queryBusPosition()
        raw_gps=[]
        for pos in pos_list:
            [gps_x,gps_y]=self.calcGPSCoord(pos['x'],pos['y'])
            raw_gps.append([gps_y,gps_x])
            pos['gps_x']=gps_x
            pos['gps_y']=gps_y
            pos['orientation']=pos['i']/5.4
            pos['bus_id']=pos['o']
            pos.pop('x')
            pos.pop('y')
            pos.pop('i')
            pos.pop('o')
        a_road=onRoad.onRoad()
        new_gps=a_road.getRoadPositions(raw_gps)
        i=0
        for pos in pos_list:
            pos['gps_y']=new_gps[i][0]
            pos['gps_x']=new_gps[i][1]
            i+=1
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
    print '----'
    #get gps location and orientation of this route
    gps_pos_list=route1.queryBusGPSPosition()
    for pos in gps_pos_list:
        print pos
    print '-----'
    gps_pos_onroad_list=route1.queryBusGPSPositionOnRoad()
    for pos in gps_pos_onroad_list:
        print pos
