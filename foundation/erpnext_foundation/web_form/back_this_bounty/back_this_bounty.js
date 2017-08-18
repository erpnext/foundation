frappe.ready(function() {
	var bounty_name = getParameterByName('bounty');
	$('input[data-fieldname="bounty_name"]').val(bounty_name);
	$('[data-fieldname="user"]').val(frappe.session.user);

	function getParameterByName(name) {
		var url = window.location.href;
		name = name.replace(/[\[\]]/g, "\\$&");
		var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
			results = regex.exec(url);
		if (!results) return null;
		if (!results[2]) return '';
		return decodeURIComponent(results[2].replace(/\+/g, " "));
	}
})