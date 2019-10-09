frappe.ready(function() {
	// bind events here
	frappe._calculate = function() {
		frappe.web_form.set_value('amount',
			parseInt(frappe.web_form.get_value('full_conference_tickets') || 0) * 6000
		)
	};

	$('.btn-form-submit').hide();

	frappe.web_form.events.on('after_load', () => {
		frappe.web_form.set_df_property('tshirt_table', 'hidden', 1);
		frappe.web_form.doc.currency = "USD"
		$('input[data-fieldname="full_conference_tickets"]').on('keyup', function() {
			frappe._calculate();
			let value = frappe.web_form.get_value('full_conference_tickets')
			if (value > 1) {
				frappe.web_form.set_df_property('tshirt_table', 'hidden', 0);
				frappe.web_form.set_df_property('tshirt_size', 'hidden', 1);
			} else {
				frappe.web_form.set_df_property('tshirt_table', 'hidden', 1);
				frappe.web_form.set_df_property('tshirt_size', 'hidden', 0);

			}
		});
		frappe._calculate();
	})

	frappe.web_form.validate = () => {
		let tickets = frappe.web_form.get_value('full_conference_tickets');
		if (tickets > 1) {
			tshirts = frappe.web_form.fields_dict.tshirt_table.get_value();
			total_tees = tshirts.reduce(function (acc, obj) { return acc + obj.quantity; }, 0);
			if (total_tees > tickets) {
				frappe.throw(`You can only choose ${tickets} T-Shirts.`)
			} else if (total_tees < tickets) {
				frappe.throw(`You have selected sizes for only ${total_tees} T-Shirts, you can choose ${tickets - total_tees} more`)
			}
		}
	}
})