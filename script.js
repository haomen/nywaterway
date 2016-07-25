//Set and show time
var currentdate = new Date();
var date_of_week = currentdate.getDay();
var current_hour = currentdate.getHours();
var current_min = currentdate.getMinutes();
//
//var date_of_week = 4;
//var current_hour = 12;
//var current_min = 20;
var current_time = current_hour+current_min/100;
var datetime = "Last Sync: " + currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/"
                + currentdate.getFullYear() + " @ "
                + current_hour + ":"
                + current_min + ":"
                + currentdate.getSeconds() +"; <br>Day of the week: "
                + date_of_week;
document.getElementById("info1").innerHTML = datetime;

//SET MAP
var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom:15,
        center: {lat: 40.759011, lng: -73.984472}
    });
    var map_styles = [
        {
        "stylers": [
              { "saturation": -46 },
              { "lightness": 12 }
            ]
        }
    ]
    map.setOptions({styles:map_styles});
         //set route
     var bus_route=new google.maps.Data();
     function getGeojsonByTime(){
        if(date_of_week==0 || date_of_week ==6){
        //week end
            document.getElementById("info2").innerHTML = "Off Peak Map";
            return "mhroutesOffpeak.geojson";
        }else if((current_time>6.10 && current_time<10.10)||(current_time>15.30 && current_time<19.10)){
        //week day peak
            document.getElementById("info2").innerHTML = "Peak";
            return "mhroutesPeak.geojson";
        }else{
            document.getElementById("info2").innerHTML = "Off Peak Map";
            return "mhroutesOffpeak.geojson";
        };
     };
     bus_route.loadGeoJson(getGeojsonByTime());
     bus_route.setMap(map);

     var setColorStyle = function(feature) {
        if(feature.getProperty('id')==33){
            return {
                 strokeColor: '	#006699',
                 strokeWeight: 4
             }
         }else{
            return {
                 strokeColor: '#79a6d2',
                 strokeWeight: 4
             }
         };
     };
     bus_route.setStyle(setColorStyle);

     // Load GeoJSON for bus locations.
     var bus_location=new google.maps.Data();
     bus_location.loadGeoJson('sample.json');
     bus_location.setMap(map);

     //style fucntions
    var setIcon = function(feature) {
        return {
             icon: {   path: "M256,60.3C147.9,60.3,60.3,147.9,60.3,256S147.9,451.7,256,451.7S451.7,364.1,451.7,256S364.1,60.3,256,60.3z   M313.1,215.4H279c1.8,33.9,3.6,67.8,5.5,101.7c0.5,9.8,1.2,19.6,1.8,29.5c1,15.3-8.5,28.9-22.7,32.4c-14.5,3.6-29.1-3.4-35.3-17.1  c-2.2-4.8-2.9-10-2.6-15.3c0.9-15.1,1.8-30.3,2.7-45.4c1.4-23.7,2.7-47.3,4-71c0.3-4.9,0.5-9.9,0.7-14.9h-34.3  c-8.3,0-12.9-9.7-7.6-16.1l5.7-8.1c14.6-20.5,30.8-39.9,48.4-58l0.3-0.3c5.3-6.5,15.2-6.5,20.5,0c17.8,18.2,34.2,37.8,49,58.6  l5.5,7.8C326,205.7,321.4,215.4,313.1,215.4z",
//                       labelOrigin:,
                       strokeColor: "#3366cc",
                       fillColor: "#404040",
                       rotation: feature.getProperty('orientation'),
                       fillOpacity:1,
//                       size: new google.maps.Size(2, 2),
                       scale: 0.05
                        }
         };
        };

    // Set the stroke width, and fill color for each polygon, with default colors at first
    bus_location.setStyle(setIcon);



     var infowin=new google.maps.InfoWindow('nyc bus is here!');
     // Set mouseover event for each feature.
     bus_location.addListener('click',function(event){
         var pos='<div text-align:center;>bus_id:'+event.feature.getProperty("bus_id")+'<br/>route_id:'+event.feature.getProperty("route_qid")+'<br/>orientation:'+event.feature.getProperty("orientation")+'<br/>lat: '+event.feature.getGeometry().get().lat().toFixed(5)+'<br/>long: '+event.feature.getGeometry().get().lng().toFixed(5)+'</div>';
         infowin.setContent(pos);
         infowin.setPosition(event.feature.getGeometry().get());
         infowin.open(map);
     });

 }