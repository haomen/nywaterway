###NY Waterway Bus Locationing
=========
Retrieve locationing data from NYWaterway API, the transform the **Location** to standard GPS coordinates. display on Google Map, predict based ETA based on currect location, alert based on given criteria.

* retrieve location from NYWaterway website:
  * request parameters:
    * time: new Date().getTime() is javascript
    * id: route of bus
    > ``https://services.saucontds.com/tds-map/nyw/nywvehiclePositions.do?id=33&time=1468116622306``
  * returned results:
    > ``[{"o":133170991,"x":87,"y":358,"i":1134},{"o":133171021,"x":88,"y":357,"i":162},{"o":133171037,"x":479,"y":551,"i":1134},{"o":133161454,"x":90,"y":360,"i":1080},{"o":133171009,"x":84,"y":371,"i":1080},{"o":133171033,"x":96,"y":341,"i":162},{"o":133170975,"x":93,"y":346,"i":1458},{"o":133171001,"x":90,"y":377,"i":162},{"o":133160419,"x":87,"y":362,"i":1134},{"o":133171007,"x":85,"y":366,"i":1026},{"o":133170983,"x":87,"y":359,"i":108},{"o":133171003,"x":633,"y":274,"i":648},{"o":133170969,"x":78,"y":372,"i":1134}] ``
    * x:
    * y:
    * z:
    * o:
* map to standard gps coordinates
