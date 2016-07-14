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
    """
    :param id: route id to request info on
    :return: a json object, and id requested
    """
    url = "https://services.saucontds.com/tds-map/nyw/nywmapTranslation.do?id=%s" % (id)
    print url
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        print 'Geting location for route %s...'%id
        return (response.read(),id)
    except urllib2.HTTPError:
        return ("HTTPError Occured","noid")
def parseresult(result,id):
    """
    :param result: http request respond json object
    :param id: route id requested on
    :return: dictionary of vars with id as key
    """
    if result == "HTTPError Occured":
        return "HTTPError Occured"
    else:
        result_object = json.loads(result)
        # result_object["id"]=id
        dict={}
        dict[id]=result_object
        print dict
        return dict

route33, this_id = GetTranslator(33)
print route33
obj36 = parseresult(route33,this_id)

route15 = GetTranslator(15)

routesTrans=[]
for i in range(0,100):
    route, this_i = GetTranslator(i)
    if this_i != "noid":
        # if route exists, parse result
        obj = parseresult(route,this_i)
        routesTrans.append(obj)

# cleanlist=[]
# for i in routesTrans:
#     if i =="HTTPError Occured":
#         continue
#     cleanlist.append(i)
# dict = {}

with open(outfile, 'w') as outfile:
    json.dump(routesTrans, outfile)
# write out
# f = open(outfile, 'wb')
# csvWriter = csv.writer(f)
# for i in routesTrans:
#     csvWriter.writerow(i)
# f.close()
print(time.strftime('%a %H:%M:%S'))
print 'End...'