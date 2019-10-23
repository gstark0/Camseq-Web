$(document).ready(function() {
    updateTime();
    updateImage();
    $('#camera-threats .value').text(cameraInfo['dangers'])
    $('#camera-warnings .value').text(cameraInfo['warnings'])
    $('#camera-name').text(cameraInfo['name']);
    $('#location').text(cameraInfo['location']);
    $('#coordinates').text(cameraInfo['coordinates']);
    $('#height').text(cameraInfo['camera_height']);

    cameraIncidents.forEach(function(incident, i) {
        icon = '';
        if(incident['type'] == 'danger')
            icon = 'fas fa-exclamation-circle';
        else
            icon = 'fas fa-exclamation-triangle';

        $('#registry-content').prepend(`
            <div class="registry-item" data-index="` + i + `">
                <i class="` + icon + `"></i>
                <span class="register-item-description">` + incident['description'] + `</span>
                <span class="register-item-date">` + incident['time'] + `</span>
            </div>
        `);
    });
});

$('#registry-content').on('click', '.registry-item', function() {
    ix = parseInt(this.getAttribute('data-index'));
    $('#camera-footage').attr('src', '../footage/' + cameraIncidents[ix]['incident_id'] + '/img.jpg');
    if(cameraIncidents[ix]['type'] == 'danger') {
        $('#type-footage i').removeClass('fas fa-exclamation-circle');
        $('#type-footage i').removeClass('fas fa-exclamation-triangle');
        $('#type-footage i').addClass('fas fa-exclamation-circle');
        $('#type-footage').css('color', '#EF1758');
        $('#type-footage span').text('Poważne zagrożenie');
    } else {
        $('#type-footage i').removeClass('fas fa-exclamation-circle');
        $('#type-footage i').removeClass('fas fa-exclamation-triangle');
        $('#type-footage i').addClass('fas fa-exclamation-triangle');
        $('#type-footage').css('color', '#FFBF45');
        $('#type-footage span').text('Ostrzeżenie');
    }
    $('#preview-modal #type').text(cameraIncidents[ix]['description']);
    $('#preview-modal-date').text(cameraIncidents[ix]['time']);

    $('#preview-modal').css('display', 'flex');
});

$('#preview-modal').on('click', '#close-preview-modal', function() {
    $('#preview-modal').hide();
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

    img_tag = new Image();
    img_tag.onload = function() {
        $('#camera-image').css('background-image', 'url("' + imgUrl + '")');
        let t = setTimeout(updateImage, 2000);
    }
    img_tag.src = imgUrl;
}

function checkTime(i) {
    if (i < 10) {i = '0' + i};
    return i;
}