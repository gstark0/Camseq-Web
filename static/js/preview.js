$(document).ready(function() {
    updateTime();
    $('#camera-name').text(cameraInfo['name']);
    $('#location').text(cameraInfo['location']);
    $('#coordinates').text(cameraInfo['coordinates']);
    $('#height').text(cameraInfo['camera_height']);

    cameraIncidents.forEach(function(incident) {
        icon = '';
        if(incident['type'] == 'danger')
            icon = 'fas fa-exclamation-circle';
        else
            icon = 'fas fa-exclamation-triangle';

        $('#registry-content').prepend(`
            <div class="registry-item">
                <i class="` + icon + `"></i>
                <span class="register-item-description">` + incident['description'] + `</span>
                <span class="register-item-date">` + incident['time'] + `</span>
            </div>
        `);
    });
});

$('#registry-content').on('click', '.registry-item', function() {
    alert(this);
});

function updateTime() {
    let today = new Date();
    let hours = today.getHours();
    let minutes = today.getMinutes();
    minutes = checkTime(minutes);

    let day = checkTime(today.getDate());
    let month = checkTime(today.getMonth()+1);
    let year = today.getFullYear();

    $('#time').text(day + '/' + month + '/' + year + ' - ' + hours + ':' + minutes);
    let t = setTimeout(updateTime, 500);
}

function checkTime(i) {
    if (i < 10) {i = '0' + i};
    return i;
}