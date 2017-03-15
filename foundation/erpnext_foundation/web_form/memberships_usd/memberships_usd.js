frappe.ready(function() {
	// bind events here
	$(".page-header-actions-block .btn-primary, .page-header-actions-block .btn-default").addClass('hidden');
	$(".text-right .btn-primary").addClass('hidden');

	var m = moment();

	var set_amount = function() {
		var membership_type = $('[data-fieldname="membership_type"]').val();
		var currency = $('[data-fieldname="currency"]').val();

		amount = {
			'Gold': 5000,
			'Silver': 1500,
			'Individual': 200
		}

		$('[data-fieldname="amount"]').val(amount[membership_type]);
	}
	
	if(get_url_arg('name')) {
		$('[data-fieldname="membership_type"]').prop('disabled', true);
		$('[data-fieldname="currency"]').prop('disabled', true);
		$('.page-content .btn-form-submit').addClass('hidden');
	} else {
		$('[data-fieldname="from_date"]').val(m.format()).trigger('change');
		$('[data-fieldname="to_date"]').val(m.add(1, 'year').format()).trigger('change');
		$('[data-fieldname="membership_type"]').on('change', function() { set_amount(); });
		$('[data-fieldname="currency"]').val('USD');
		set_amount();
	}
})