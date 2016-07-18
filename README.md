###NY Waterway Bus Locationing
---------
Retrieve locationing data from NYWaterway API, the transform the **Location** to standard GPS coordinates. display on Google Map, predict based ETA based on currect location, alert based on given criteria.

* retrieve location from NYWaterway website: >nywBusPos.py
    * retrieve raw data as json format from nywaterway website: >queryBusPosition()
      * x: x relative position on the route image
      * y: y relative position on the route image
      * i: bus orientation (0-3600), no idea why using i for orientation and o for bus_id
      * o: bus id, only last for digit make sense
    * retrieve bus gps coordinates as json format: >queryBusGPSPosition()
      * gps_x, gps\_y, orientation, bus\_id
      
