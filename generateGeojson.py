#!/usr/bin/env python

import sys
import MySQLdb
if __name__=="__main__":
    if len(sys.argv)!=3:
        print 'should be\n'+sys.argv[0]+' <sql select query> <output.json>'
        sys.exit(1)

    sql_query=sys.argv[1]
    of=open(sys.argv[2],'w')

    # write top header
    of.write('''{\n"type":"FeatureCollection",\n''')
    of.write('''"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },\n\n"features": [\n''')

    db=MySQLdb.connect('localhost','nywaterway','nywaterway','nywaterway')
    cursor=db.cursor()
    cursor.execute(sql_query)
    #print cursor.rowcount
    for i in range(cursor.rowcount-1):
        row=cursor.fetchone()
        route_qid=str(row[1])
        busid=str(row[2])
        lon=str(row[3])
        lat=str(row[4])
        orientation=str(row[5])
        of.write('''{ "type": "Feature", "properties":{"route_qid":'''+route_qid+", \"bus_id\":"+busid+",\"orientation\":"+orientation+'''}, "geometry": { "type": "Point", "coordinates": ['''+lon+','+lat+''']}},\n''')

    row=cursor.fetchone()
    route_qid=str(row[1])
    busid=str(row[2])
    lon=str(row[3])
    lat=str(row[4])
    orientation=str(row[5])
    of.write('''{ "type": "Feature", "properties":{"route_qid":'''+route_qid+", \"bus_id\":"+busid+",\"orientation\":"+orientation+'''}, "geometry": { "type": "Point", "coordinates": ['''+lon+','+lat+''']}}\n''')

    of.write(']\n}\n')
    of.close()
