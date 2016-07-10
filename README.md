NY Waterway Bus Locationing
=========
Retrieve locationing data from NYWaterway API, the transform the **Location** to standard GPS coordinates. display on Google Map, predict based ETA based on currect location, alert based on given criteria.
    1. retrieve location from NYWaterway website:
    >curl 'https://services.saucontds.com/tds-map/nyw/nywvehiclePositions.do?id=33&time=1468116622306' -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.5' -H 'Connection: keep-alive' -H 'Cookie: mobile=false; mobile=false; __utma=86100378.1188898332.1463792940.1463792940.1468116573.2; __utmz=86100378.1468116573.2.2.utmcsr=nywaterway.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=86100378.3.10.1468116573; __utmc=86100378; __utmt=1; mobile=false' -H 'Host: services.saucontds.com' -H 'Referer: https://services.saucontds.com/tds-map/nyw/routemapc.htm?id=33' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'
    2. map to standard gps coordinates
