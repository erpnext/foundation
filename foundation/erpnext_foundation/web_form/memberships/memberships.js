frappe.ready(function() {
	// bind events here
	var set_amount = function() {
		var membership_type = $('[data-fieldname="membership_type"]').val();
		var currency = $('[data-fieldname="currency"]').val();
		if(currency=='USD') {
			amount = {
				'Gold': 5000,
				'Silver': 1500,
				'Individual': 200
			}
		} else {
			amount = {
				'Gold': 300000,
				'Silver': 100000,
				'Individual': 10000
			}
		}
		var currency = $('[data-fieldname="amount"]').val(amount[membership_type]);
	}

	if(get_url_arg('name')) {
		$('[data-fieldname="membership_type"]').prop('disabled', true);
		$('[data-fieldname="currency"]').prop('disabled', true);
		$('.page-content .btn-form-submit').addClass('hidden');
 	} else {
		var m = moment();
		$('[data-fieldname="from_date"]').val(m.format()).trigger('change');
		$('[data-fieldname="to_date"]').val(m.add(1, 'year').format()).trigger('change');
		$('[data-fieldname="membership_type"]').on('change', function() { set_amount(); });
		$('[data-fieldname="currency"]').val('USD')
			.on('change', function() {
				set_amount();
			})
			.trigger('change');
 	}
})

