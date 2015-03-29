$(document).ready(function() {
	$('#test-button').click(function() {
		console.log('Button clicked!');

		$.get('https://lahuang4.scripts.mit.edu:444/sleep/auth.php', function(response) {
			console.log(response);
			console.log('received!');
		});
	});
});