

import nywBusPos
import csv
data= [{"o":133170989,"x":84,"y":363,"i":1134},{"o":133171009,"x":83,"y":371,"i":1188},{"o":133171021,"x":430,"y":340,"i":1350},{"o":133170979,"x":87,"y":359,"i":1242},{"o":133171005,"x":90,"y":353,"i":1134},{"o":133171027,"x":80,"y":371,"i":1134},{"o":133171035,"x":82,"y":366,"i":1134},{"o":133171015,"x":96,"y":340,"i":1512},{"o":133171003,"x":85,"y":366,"i":162},{"o":133170973,"x":83,"y":366,"i":1188},{"o":133170991,"x":86,"y":364,"i":162},{"o":133171037,"x":87,"y":361,"i":1188},{"o":133171007,"x":86,"y":365,"i":1188},{"o":1030000300,"x":86,"y":361,"i":1134},{"o":945250838,"x":85,"y":367,"i":1080},{"o":133161454,"x":89,"y":362,"i":1080},{"o":133170961,"x":90,"y":358,"i":162},{"o":133171023,"x":498,"y":535,"i":1080}]


#
# d = {}
# l=[]
# with open("NYWtranslator100.txt") as f:
#     for line in f:
#         l=line
#         d=line
#         a=1
#        # (key, val) = line.split()
#        # d[int(key)] = val
# print d
#
# def read(name):
#     res = {}
#     with open(name,"r") as text:
#         dict_from_file = eval(text.read())
#     return dict_from_file
# dict = read("NYWtranslator100.txt")
# print dict
#
# len = len(dict)
# routes={}
#
# for i in dict:
#     print i
#     print i.keys()
#     key = i.keys()[0]
#     routes.update({key: i[key]})
# print routes
#
# print routes['33']
route1=nywBusPos.nywBusPos(33)
translated = route1.queryBusGPSPosition(False,data)
print translated

# write out
outfile="ny33list_tograph1145.csv"
f = open(outfile, 'wb')
csvWriter = csv.writer(f)
header = ["orin","id","long","lat"]
csvWriter.writerow(header)
for i in translated:
    listtooutput=i.values()
    print listtooutput
    csvWriter.writerow(listtooutput)
f.close()