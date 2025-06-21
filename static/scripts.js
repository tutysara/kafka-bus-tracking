var map = L.map("map").setView([12.837048877381548, 77.69724319681171], 13);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);
//var marker = L.marker([51.5, -0.09]).addTo(map);
//marker.bindPopup("<b>Chaitanya</b><br>school bus").openPopup();

const TOPICNAME = "tbus-data";
var mapMarkers = {};
var lineToBusNames = {
  "001": "Brook Field",
  "002": "SFS",
  "003": "St. Joseph Cham",
};

var event_source = new EventSource("/topic/" + TOPICNAME);
console.log("event_source=", event_source);
event_source.addEventListener(
  "message",
  function (e) {
    var data = JSON.parse(e.data);
    console.log("data=", data);
    if (mapMarkers[data.busline]) {
      map.removeLayer(mapMarkers[data.busline]);
    }
    var marker = L.marker([data.latitude, data.longitude]).addTo(map);
    var schoolName = lineToBusNames[data.busline];
    marker.bindPopup("<b>" + schoolName + "</b><br>school bus").openPopup();
    //marker.bindPopup("<b>" + schoolName + "</b><br>school bus");

    mapMarkers[data.busline] = marker;
  },
  false,
);
