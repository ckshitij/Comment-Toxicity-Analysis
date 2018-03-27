$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#enginetext').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			if (data.toxic) {
				$('#ans').text(data.toxic).show();
			}
			else if(data.error){
				$('#ans').text(data.error).show();
			}

		});

		event.preventDefault();

	});

});