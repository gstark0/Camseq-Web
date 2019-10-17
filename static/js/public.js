
var mymap = L.map('mapid').setView([52.2319237, 21.0067265], 13);

L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png', {
    attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18,
    id: 'mapbox.streets',
}).addTo(mymap);

var heat = L.heatLayer([
	[52.2319237,  21.0067265, 10],
], {radius: 10}).addTo(mymap);