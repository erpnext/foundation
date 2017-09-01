/* eslint-disable */
// rename this file from _test_[name] to test_[name] to activate
// and remove above this line

QUnit.test("test: Portal Job", function (assert) {
	let done = assert.async();

	// number of asserts
	assert.expect(1);
	let done = assert.async();
	frappe.run_serially([
		// insert a new Portal Job
		() => {
			return frappe.tests.make('Portal Job', [
				// values to be set
				{title: 'test123'},
				{company_name:'Test Company'},
				{status:'Open'},
				{description:'Test Content'},
				{contact_number:'123456789'},
				{route:'test'}
			]);
		},
		() => cur_frm.save(),
		() => {
			assert.equal(cur_frm.doc.title, 'test123');
		},
		() => done()
	]);
});