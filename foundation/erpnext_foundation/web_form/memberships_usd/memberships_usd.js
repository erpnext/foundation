frappe.ready(function() {
	// bind events here
	form = frappe.web_form.fields_dict;

	// $(".page-header-actions-block .btn-primary, .page-header-actions-block .btn-default").addClass('hidden');
	// $(".text-right .btn-primary").addClass('hidden');

	frappe._set_values = function() {
		let from_date = get_date();
		let to_date = get_date(1);

		frappe.web_form.set_value('from_date', from_date);
		frappe.web_form.set_value('to_date', to_date);

		let membership_type = $('input[data-fieldname="membership_type"]').val();
		amount = {
			'Gold': 5000,
			'Silver': 1500,
			'Individual': 200
		}
		frappe.web_form.set_value('amount', amount[membership_type]);
	}

	var get_date = (add_year = 0) => {
		const today = new Date();
		const year = today.getFullYear() + add_year;
		const month = ((today.getMonth() + 1) + '').padStart(2, '0');
		const day = today.getDate();
		return year + '-' + month + '-' + day;
	}

	frappe.web_form.events.on('after_load', () => {
		frappe.web_form.set_value('currency', 'USD');
		if(frappe.utils.get_url_arg('name')) {
			$('input[data-fieldname="membership_type"]').prop('disabled', true);
			$('input[data-fieldname="currency"]').prop('disabled', true);
			$('.page-content .btn-form-submit').addClass('hidden');
		} else {
			form.membership_type.$input.on('change', () => frappe._set_values());
			form.membership_type.$input.on('focusout', () => frappe._set_values());
			frappe._set_values();
		}
	})

	frappe.web_form.validate = () => frappe._set_values();
})
