#!/usr/bin/env python

import nywBusPos
import MySQLdb
import sys,time,datetime

def writePos2Mysql(route_id,pos):
    db=MySQLdb.connect("localhost","nywaterway","nywaterway","nywaterway")
    cursor=db.cursor()

    for pos in pos_list:
        sql_query="INSERT INTO bus_location (route_id,bus_id,gps_x,gps_y,orientation,update_time) values("+route_id+','+str(pos["bus_id"])+","+str(pos["gps_x"])+","+str(pos["gps_y"])+","+str(pos["orientation"])+",now())"
        try:
            cursor.execute(sql_query)
            db.commit()
        except Exception as e:
            print "error when writing into db:"+e
            db.rollback()

    db.close()

if __name__=='__main__':
    if len(sys.argv)!=2:
        print 'should be:\n'+sys.argv[0]+' <route id>'
        sys.exit(1)

    #make query every 30 seconds
    a_route=nywBusPos.nywBusPos(int(sys.argv[1]))
    while True:
        print "querying route "+sys.argv[1]+" at time "+str(datetime.datetime.now())
        pos_list=a_route.queryBusGPSPositionOnRoad()
        writePos2Mysql(sys.argv[1],pos_list)
        time.sleep(30)
