frappe.ready(function() {
	// bind events here
	form = frappe.web_form.fields_dict;

	// $(".page-header-actions-block .btn-primary, .page-header-actions-block .btn-default").addClass('hidden');
	// $(".text-right .btn-primary").addClass('hidden');

	frappe._set_values = function() {
		let from_date = frappe.datetime.now_date();
		let to_date = frappe.datetime.add_months(from_date, 12)

		frappe.web_form.set_value('from_date', from_date);
		frappe.web_form.set_value('to_date', to_date);

		let membership_type = $('input[data-fieldname="membership_type"]').val();
		amount = {
			'Gold': 300000,
			'Silver': 100000,
			'Individual': 10000
		}
		frappe.web_form.set_value('amount', amount[membership_type]);
	}

	frappe.web_form.events.on('after_load', () => {
		frappe.web_form.set_value('currency', 'INR');
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
