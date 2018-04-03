frappe.ready(function() {
	let page = $(document);
	page.find('.web-form-page div .text-right button')
		.removeClass('btn-primary btn-sm')
		.addClass('button-primary')
		.empty().append("Apply");

	// Minimize cancel grid
	let grid_cancel = page.find('.web-form-grid-row td');
	for (let i in grid_cancel) {
		if (grid_cancel[i].style && grid_cancel[i].style.width == '8.3333%') {
			grid_cancel[i].style.width = "1%";
		}
	}

	// Add Section heading
	$(`<h2 class="heading-2"> Candidate Detail </h2>`)
		.insertBefore(page.find('.web-form-page .section').first());
	$(`<h2 class="heading-2"> Education Detail </h2>`)
		.insertBefore(page.find('.web-form-page .section:nth-child(3)'));
	$(`<h2 class="heading-2"> Project Detail </h2>`)
		.insertBefore(page.find('.web-form-page .section:nth-child(5)'));

	// Make textarea's height adapt to content
	page.find('textarea').css("height", "auto");
	page.find('textarea').css("min-height", "100px");

	// checkbox tweak
	let x = page.find('div.checkbox');
	x.removeClass('checkbox').addClass('checkbox-inline');
	let y = page.find('div .checkbox-inline label');
	$(`<a style="display: inline-block;" href="/esoc/terms-and-rules" target="_blank"> terms & rules </a>`)
		.appendTo(y[0]);

})