

import csv

data= [{"o":133171035,"x":413,"y":297,"i":162},
       {"o":133170989,"x":384,"y":443,"i":648},
       {"o":133170969,"x":88,"y":355,"i":162},
       {"o":133171023,"x":91,"y":351,"i":1296},
       {"o":133171017,"x":82,"y":373,"i":1134},
       {"o":133171021,"x":93,"y":347,"i":1566},
       {"o":133171027,"x":84,"y":362,"i":1134},
       {"o":133171029,"x":88,"y":357,"i":1242},
       {"o":133170981,"x":82,"y":369,"i":972},
       {"o":133160419,"x":85,"y":364,"i":1134},
       {"o":133170993,"x":86,"y":358,"i":1134},
       {"o":133171037,"x":461,"y":352,"i":1620}]


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

def read(name):
    res = {}
    with open(name,"r") as text:
        dict_from_file = eval(text.read())
    return dict_from_file
dict = read("NYWtranslator100.txt")
print dict

len = len(dict)
routes={}

for i in dict:
    print i
    print i[0]

