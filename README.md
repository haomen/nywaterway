###NY Waterway Bus Locationing
---------
Retrieve locationing data from NYWaterway API, the transform the **Location** to standard GPS coordinates. display on Google Map, predict based ETA based on currect location, alert based on given criteria.

* retrieve location from NYWaterway website:
  * request parameters:
    * time: new Date().getTime() is javascript
    * id: route of bus
    > Example: ``https://services.saucontds.com/tds-map/nyw/nywvehiclePositions.do?id=33&time=1468116622306``
  * returned results:
    * x:
    * y:
    * z:
    * o:
* map to standard gps coordinates
    * take 57st for example, id=33. time=new Date().gettime()
    * gps_x=(x-0.5)*5.32196e-5-74.007868
    * gps_y=-(y-0.5)*4.03097e-5+40.774535
