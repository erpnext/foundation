// Copyright (c) 2017, EOSSF and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bounty', {
	refresh: function(frm) {

	},
	feature_name: function(frm) {
		if (frm.doc.route) return;
		const route = 'bounty/' + frm.doc.feature_name.toLowerCase().replace(/ /g, '-');
		frm.set_value('route', route);
	}
});
