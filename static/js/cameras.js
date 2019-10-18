$(document).ready(function() {
	camerasList.forEach(function(c) {
		console.log(c)
		$('#cameras-list').append(`
			<div class="camera-item">
                <div class="camera-item-left">
                    <span class="camera-item-name">` + c['name'] + `</span>
                    <span class="camera-item-location">` + c['location'] + `</span>
                </div>
                <div class="camera-item-right">
                    <div class="camera-item-alerts threat">
                        <i class="fas fa-exclamation-circle"></i>
                        <span>0</span>
                    </div>
                    <div class="camera-item-alerts warning">
                        <i class="fas fa-exclamation-triangle"></i>
                        <span>0</span>
                    </div>
                </div>
            </div>
		`)
	})
});