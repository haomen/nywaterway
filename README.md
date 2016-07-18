###NY Waterway Bus Locationing
---------
Retrieve locationing data from NYWaterway API, the transform the **Location** to standard GPS coordinates. display on Google Map, predict based ETA based on currect location, alert based on given criteria.

* retrieve location from NYWaterway website: 
    >nywBusPos.py
    * retrieve raw data as json format from nywaterway website: 
      >queryBusPosition()
      * x: x relative position on the route image
      * y: y relative position on the route image
      * i: bus orientation (0-3600), no idea why using i for orientation and o for bus_id
      * o: bus id, only last for digit make sense
    * retrieve bus gps coordinates as json format: 
      >queryBusGPSPosition()
      * gps_x, gps\_y, orientation, bus\_id
      
* NYwaterway bus route id meaning:
  According to nywaterway Peak Buses Master Map(http://nywaterway.com/UserFiles/Files/Peak%20Bus%20Map.pdf). 
  Peak Hours:    6:10AM-10:10AM, 3:30PM-7:10PM
  Offpeak Hours: 10:10AM-3:30PM, 7:10PM-12:30AM
  For Peak hour, they have 57st route, 50st route, 42 st route,34 st route, downtown local am route, downtown local pm route. 
  For offpeak hour, they have 42/34 st route, 44/57 st route, 50/57 st route, lincoln center route, and downtown combo route.
  *  1: Peak 34 st Manhattan route 
  * 21: Peak 42 st Manhattan route
  * 22: Peak 50 st Manhattan route
  * 32: Peak 57 st Manhattan route
  * 40: Peak downtown local AM route
  * 43: Peak downtown local PM route
  * 33: Offpeak 44/57 st Manhattan route
  * 34: Offpeak 50/57 st Manhattan offpeak route
  * 36: Offpeak 34/42 st Manhattan offpeak route
  * 42: Offpeak Downtown combo Manhattan offpeak route
  * 38: Offpeak Lincoln center route.
  
  
