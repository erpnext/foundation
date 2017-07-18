frappe.ready(function() {
	// bind events here
	var calculate = function() {
		var amount =
			(parseInt($('input[name="full_conference_tickets"]').val() || 0) * 50)
			+ (parseInt($('input[name="user_conference_tickets"]').val() || 0) * 10);
		$('input[name="amount"]').val(amount);
		$('input[name="amount"]').closest('.form-group').toggleClass('has-error', amount == 0);
	};

	$('input[name="full_conference_tickets"]').on('keyup', function() {
		calculate();
	});
	$('input[name="user_conference_tickets"]').on('keyup', function() {
		calculate();
	});

	$('.btn-form-submit').hide();
})