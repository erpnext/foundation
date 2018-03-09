import frappe

no_cache = 1
def get_context(context):
	context.form_dict = frappe.form_dict
	context.title = 'Service Providers'
	context.gold_members = []

	if frappe.form_dict.country:
		context.parents = [dict(label='All Service Providers',
			route='service-providers', title='All Service Providers')]

	filters = dict()
	filters['show_in_website'] = 1
	if frappe.form_dict.country:
		filters['country'] = frappe.form_dict.country

	gold_members = [d.name for d in frappe.get_all('Member', dict(membership_type='Gold'))]
	if gold_members:
		filters['member'] = ('in', gold_members)
		context.gold_members = frappe.get_all('Service Provider', 'title, introduction, `image`, route',
			filters)

	if context.gold_members:
		context.has_gold_member = 1
	else:
		context.gold_members.append(dict(
			title='Your Company',
			introduction='Become a Gold Member today and get your company featured here',
			image='/assets/foundation/img/gold.png',
			route='/members',
			placeholder=True
		))

	context.silver_members = []
	silver_members = [d.name for d in frappe.get_all('Member', dict(membership_type='Silver'))]
	if silver_members:
		filters['member'] = ('in', silver_members)
		context.silver_members = frappe.get_all('Service Provider', 'title, introduction, `image`, route',
			filters, debug=1)

	if context.silver_members:
		context.has_silver_member = 1
	else:
		context.silver_members.append(dict(
			title='Your Company',
			introduction='Become a silver Member today and get your company featured here',
			image='/assets/foundation/img/silver.png',
			route='/members',
			placeholder=True
		))

	context.individual_members = []
	individual_members = [d.name for d in frappe.get_all('Member',
		dict(membership_type='Individual'))]
	if individual_members:
		filters['member'] = ('in', individual_members)
		context.individual_members = frappe.get_all('Service Provider',
			'title, introduction, `image`, route', filters)

	if context.individual_members:
		context.has_individual_member = 1
	else:
		context.individual_members.append(dict(
			title='Your Company',
			introduction='Become an invidual member to list here',
			route='/members'
		))

	if context.form_dict.country:
		context.title = 'ERPNext Service Providers in {0}'.format(context.form_dict.country)

		context.service_providers = [d for d in frappe.get_all('Service Provider', 'name, title, introduction, `image`, route',
			dict(country=frappe.form_dict.country, show_in_website=1), order_by='name') if d.name not in individual_members]

	else:
		# countries
		context.countries = frappe.db.sql('''select
				distinct country, count(*)
			from
				`tabService Provider`
			where
				show_in_website = 1
			group by
				country
			order by
				country''')
