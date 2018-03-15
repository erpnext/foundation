frappe.ready(function() {
	// bind events here
	$(".page-header-actions-block .btn-primary, .page-header-actions-block .btn-default").addClass('hidden');
	$(".text-right .btn-primary").addClass('hidden');

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
	var get_date = (add_year = 0) => {
		const today = new Date();
		const year = today.getFullYear() + add_year;
		const month = ((today.getMonth() + 1) + '').padStart(2, '0');
		const day = today.getDate();
		return year + '-' + month + '-' + day;
	}


	if(frappe.utils.get_url_arg('name')) {
		$('[data-fieldname="membership_type"]').prop('disabled', true);
		$('[data-fieldname="currency"]').prop('disabled', true);
		$('.page-content .btn-form-submit').addClass('hidden');
	} else {
		const from_date = get_date();
		const to_date = get_date(1);
		$('[data-fieldname="from_date"]').val(from_date).trigger('change');
		$('[data-fieldname="to_date"]').val(to_date).trigger('change');
		$('[data-fieldname="membership_type"]').on('change', function() { set_amount(); });
		$('[data-fieldname="currency"]').val('USD');
		set_amount();
	}
})