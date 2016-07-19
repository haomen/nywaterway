#!/usr/bin/env python

import sys
import MySQLdb
if __name__=="__main__":
    if len(sys.argv)!=2:
        print 'should be\n'+sys.argv[0]+' <sql select query>'
        sys.exit(1)

    sql_query=sys.argv[1]
    of=open('test33p_js.geojson','w')

    # write top header
    of.write('''data={\n"type":"FeatureCollection",\n''')
    of.write('''"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },\n\n"features": [\n''')

    db=MySQLdb.connect('localhost','nywaterway','nywaterway','nywaterway')
    cursor=db.cursor()
    cursor.execute(sql_query)
    #print cursor.rowcount
    for i in range(cursor.rowcount):
        row=cursor.fetchone()
        lon=str(row[3])
        lat=str(row[4])
        of.write('''{ "type": "Feature", "geometry": { "type": "Point", "coordinates": ['''+lon+','+lat+''']}},\n''')
    of.write(']\n}\n')
    of.close()
