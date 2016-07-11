###NY Waterway Bus Locationing
=========
Retrieve locationing data from NYWaterway API, the transform the **Location** to standard GPS coordinates. display on Google Map, predict based ETA based on currect location, alert based on given criteria.

* retrieve location from NYWaterway website:
  ** request parameters:
  *** time: new Date().getTime() is javascript
  *** id: route of bus
  
    >https://services.saucontds.com/tds-map/nyw/nywvehiclePositions.do?id=33&time=1468116622306
* map to standard gps coordinates
