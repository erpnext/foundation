frappe.ready(function() {
	setTimeout(() => {
		if ($('select[name=user]').val() === "") {
			window.location.href = '/bounties';
		}
	}, 1000);
})