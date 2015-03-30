$(document).ready(function() {
	$.get('https://lahuang4.scripts.mit.edu:444/sleep/auth.php', function(response) {
		console.log(response);
		console.log('received!');

		// Make POST request with CSRF token, as documented here:
		// https://docs.djangoproject.com/en/dev/ref/csrf/

		// Get CSRF token
		var csrftoken = $.cookie('csrftoken');

		function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
	    }
		});

		$.ajax({
			type: 'POST',
			data: response,
			url: window.location.href,
			dataType: 'text'
		}, function(postResponse) {
			console.log('did a POST request');
		});
	});
});