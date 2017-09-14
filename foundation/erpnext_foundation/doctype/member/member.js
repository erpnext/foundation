// Copyright (c) 2016, EOSSF and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member', {
	refresh: function(frm) {
		frappe.call({
			method:"frappe.client.get_value",
			args:{
				'doctype':"Membership",
				'filters':{'member': frm.doc.name},
				'fieldname':[
					'to_date'
				]
			},
			callback: function (data) {
				frappe.model.set_value(frm.doctype,frm.docname, "expires_on", data.message.to_date);
			}
		});


	}
});
