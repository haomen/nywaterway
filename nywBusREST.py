#!/usr/bin/env python

# 2 threads running at the same time:
# Thread #1:
# query routes and get positions into a global dictionary
#
# Thread #2:
# collect data from current position pool and return as geojson format to http query

from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
from nywBusPos import nywBusPos
import json,thread,time,datetime,MySQLdb,os,logging

app = Flask(__name__)
api = Api(app)

bus_pool={}
interval=10
route_ids=[1,21,22,32,43]

logger=logging.getLogger('nywaterway')
hdlr=logging.FileHandler('/t2/devs/nywaterway/logs/nywaterway-'+str(datetime.datetime.now().date())+'-'+str(datetime.datetime.now().time())+'.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

def busPos2GeoJson(bus_pos):
    bus_gj={}
    bus_gj.update({"type":"FeatureCollection"})
    bus_gj.update({"crs":
                   { "type": "name",
                     "properties":
                     { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }
                   }
    })
    bus_gj.update({"features":[]})
    for k,v in bus_pos.iteritems():
        bus_point={
            "geometry":{
                "coordinates":[
                    v["lng"],v["lat"]
                ],
                "type":"Point"
            },
            "properties":{
                "bus_id":k,
                "orientation":v["ori"],
                "route_qid":v["bid"],
                "last_update":v["last_update"]
            },
            "type":"Feature"
        }
        bus_gj["features"].append(bus_point)
    return bus_gj

def getAllBusLocations():
    #init route id depend on time
    #query buslocation from all route id,get all bus location at this time
    #update pos_pool
    while True:
        logger.info('refresh bus locations at:\t'+str(datetime.datetime.now()))
        db=MySQLdb.connect("localhost","nywaterway","nywaterway","nywaterway")
        cursor=db.cursor()
        for route_id in route_ids:
            #print route_id
            a_route=nywBusPos(route_id)

            try:
                bus_pos_on_route=a_route.queryBusGPSPositionOnRoad()
            except Exception as e:
                logger.error("error get bus positions: "+e)

            bus_pos_item={}
            for bus_pos in bus_pos_on_route:
                #print bus_pos
                bus_pos_item.update({
                    bus_pos["bus_id"]:
                    {
                        "lat":bus_pos["gps_y"],
                        "lng":bus_pos["gps_x"],
                        "ori":bus_pos["orientation"],
                        "bid":route_id,
                        "last_update":datetime.datetime.now()
                    }
                })
                #insert points into db
                sql_query="INSERT INTO bus_location (route_id,bus_id,gps_x,gps_y,orientation,update_time) values("+str(route_id)+','+str(bus_pos["bus_id"])+","+str(bus_pos["gps_x"])+","+str(bus_pos["gps_y"])+","+str(bus_pos["orientation"])+",now())"
                try:
                    cursor.execute(sql_query)
                    db.commit()
                except Exception as e:
                    logger.error("error writing record into db "+e)
                    db.rollback()
            if not bus_pos_item:
                logger.info("not getting any bus positions this time!")
            else:
                bus_pool.update(bus_pos_item)

        db.close()
        time.sleep(interval)

def checkTime():
    while True:
        if datetime.datetime.now().time()>datetime.time(23,00,00):
            logger.info('time is up, time to go to sleep today, exit now..')
            os._exit(1)
        time.sleep(interval)

class NywBusPosService(Resource):
    def get(self, route_id):
        #a_route=nywBusPos(int(route_id))
        #return jsonify(a_route.queryBusGPSPositionORGeojson())
        logger.info(len(bus_pool))
        return jsonify(busPos2GeoJson(bus_pool))



if __name__ == '__main__':

    # start web server
    api.add_resource(NywBusPosService, '/nywaterway/<string:route_id>')
    thread.start_new_thread(getAllBusLocations,())
    thread.start_new_thread(checkTime,())

    app.logger.addHandler(hdlr)
    app.run(host='0.0.0.0',port=30444)
    # while True:
    #     pass
    # a_map=NywBusQueryPos()
    # a_map.getAllBusLocations()
    # js=busPos2GeoJson(bus_pool)
    # print js
