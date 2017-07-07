frappe.ready(function() {
	// bind events here
	var calculate = function() {
		var amount = parseInt($('input[name="full_conference_tickets"]').val() || 0) * 3000
			+ parseInt($('input[name="user_conference_tickets"]').val() || 0) * 600;
		$('input[name="amount"]').val(amount);
	};

	$('input[name="full_conference_tickets"]').on('keyup', function() {
		calculate();
	});
	$('input[name="user_conference_tickets"]').on('keyup', function() {
		calculate();
	});

	$('.btn-form-submit').hide();
})