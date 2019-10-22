
var mymap = L.map('mapid').setView(coordList[0], 15);

L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png', {
    attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18,
    id: 'mapbox.streets',
}).addTo(mymap);

var heat = L.heatLayer([coordList[0]], {radius: 25, maxZoom: 14}).addTo(mymap);

mymap.on('moveend', loadData);

function loadData() {
    let loc = mymap.getCenter();
    fetch('/region?lat=' + loc['lat'] + '&lon=' + loc['lng'])
    .then(resp => resp.json())
    .then(resp => {
        $('#city').text(resp['city']);
        $('#region').text(resp['district']);

        let fires = resp['fires'];
        let weapons = resp['weapons'];
        let fights = resp['fights'];
        let crashes = resp['car_crashes'];

        $('#fires').text(fires);
        $('#weapons').text(weapons);
        $('#fights').text(fights);
        $('#crashes').text(crashes);

        if(fires == 'Brak danych') {
            let infoPanelStatus = $('#info-panel-status');
            infoPanelStatus.text('Nieznane');
            infoPanelStatus.css('background-color', '#737373');
            $('#safety-dot').css('background-color', '#737373');
        } else if((fires >= 2 && fires < 4)  || (weapons >= 2 && weapons < 4) || (fights >= 2 && fights < 4) || (crashes >= 2 && crashes < 4)) {
            let infoPanelStatus = $('#info-panel-status');
            infoPanelStatus.text('Średnie');
            infoPanelStatus.css('background-color', '#d17f28');
            $('#safety-dot').css('background-color', '#d17f28');
        } else if(fires > 4 || weapons > 4 || fights > 4 || crashes > 4) {
            let infoPanelStatus = $('#info-panel-status');
            infoPanelStatus.text('Niebezpiecznie');
            infoPanelStatus.css('background-color', '#FE4155');
            $('#safety-dot').css('background-color', '#FE4155');
        } else {
            let infoPanelStatus = $('#info-panel-status');
            infoPanelStatus.text('Bezpiecznie');
            infoPanelStatus.css('background-color', '#36B250');
            $('#safety-dot').css('background-color', '#36B250');
        }
    });
}

loadData();
