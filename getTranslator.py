"""
GEt the translator, save to file
"""

import sys, time
import csv, urllib2, json

print 'now we are starting...'


outfile = "NYWtranslator100.txt"
print " outfile: %s" % ( outfile)



def getTrans(id):
    app_id = "19fc66cd"
    app_key = "9696990e3f441c70c1c90b3d3955f3a5"
    domain = "https://api.cityofnewyork.us/geoclient/v1"
    url_template="%s/address.json?houseNumber=%s&street=%s&zip=%s&app_id=%s&app_key=%s"%(domain,houseNumber,street,zip,app_id,app_key)
    url2 = url_template.replace(" ", "%20")
    print url2
    data = urllib2.urlopen(url2)
    result = data.read()
    return result

def GetTranslator(id):
    url = "https://services.saucontds.com/tds-map/nyw/nywmapTranslation.do?id=%s" % (id)
    print url
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        print 'Geting location for route %s...'%id
        return response.read()
    except urllib2.HTTPError:
        return "HTTPError Occured"
def parseresult(result):
    if result == "HTTPError Occured":
        return "HTTPError Occured"
    else:
        result_object = json.loads(result)
        return result_object

route36 = GetTranslator(36)
obj36 = parseresult(route36)

route15 = GetTranslator(15)

routesTrans=[]
for i in range(100,200):
    route = GetTranslator(i)
    obj = parseresult(route)
    routesTrans.append(obj)

cleanlist=[]
for i in routesTrans:
    if i =="HTTPError Occured":
        continue
    cleanlist.append(i)

with open(outfile, 'w') as outfile:
    json.dump(cleanlist, outfile)
# write out
# f = open(outfile, 'wb')
# csvWriter = csv.writer(f)
# for i in routesTrans:
#     csvWriter.writerow(i)
# f.close()
print(time.strftime('%a %H:%M:%S'))
print 'End...'