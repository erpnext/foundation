frappe.ready(function() {
	// bind events here
	frappe._calculate = function() {
		frappe.web_form.set_value('amount',
			parseInt(frappe.web_form.get_value('full_conference_tickets') || 0) * 4000
		)
	};

	setTimeout(() => {
		$('input[data-fieldname="full_conference_tickets"]').on('keyup', function() {
			frappe._calculate();
		});
		frappe._calculate();
	}, 1000);

	$('.btn-form-submit').hide();
})