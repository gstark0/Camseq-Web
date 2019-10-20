$(document).ready(function() {
    updateTime();
    updateImage();
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
    let seconds = today.getSeconds();
    minutes = checkTime(minutes);
    seconds = checkTime(seconds);

    let day = checkTime(today.getDate());
    let month = checkTime(today.getMonth()+1);
    let year = today.getFullYear();

    $('#time').text(day + '/' + month + '/' + year + ' - ' + hours + ':' + minutes + ':' + seconds);

    let t = setTimeout(updateTime, 1000);
}

function updateImage() {
    let imgUrl = cameraInfo['url'] + '?r=' + new Date().getTime();
    $('#camera-image').css('background-image', 'url("' + imgUrl + '")');

    let t = setTimeout(updateImage, 10000)
}

function checkTime(i) {
    if (i < 10) {i = '0' + i};
    return i;
}