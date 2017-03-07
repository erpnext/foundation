import frappe

from frappe.database import Database
from markdown2 import markdown

def migrate():
	frappe.flags.mute_emails = True
	source = Database(user='095452c6b4', password='FLpERmWJGuh4N3Eb')

	# users = source.sql('select * from tabUser', as_dict=1)
	# for u in users:
	# 	frappe.get_doc(dict(
	# 		doctype='User',
	# 		name=u.name,
	# 		first_name=u.first_name,
	# 		last_name=u.last_name,
	# 		email=u.email
	# 	)).insert(ignore_if_duplicate=True)
	# 	print u.name

	# frappe.db.sql('delete from `tabService Provider`')
	# partners = source.sql('select * from `tabFrappe Partner`', as_dict=True)
	# for p in partners:
	# 	d = frappe.get_doc(dict(
	# 		doctype='Service Provider',
	# 		title=p.partner_name,
	# 		country=p.country,
	# 		image=p.logo,
	# 		introduction=p.introduction,
	# 		details=markdown(p.description),
	# 		address=p.partner_address,
	# 		discuss_ids=p.community_members,
	# 		website=p.partner_website,
	# 		github_id=p.github_id,
	# 		owner=p.owner,
	# 		creation=p.creation,
	# 		email= p.email,
	# 		phone=p.phone,
	# 		route=p.route,
	# 		show_in_website=p.show_in_website
	# 	)).insert(ignore_if_duplicate=True, ignore_mandatory=True)
	# 	print d.name

	# jobs = source.sql('select * from `tabFrappe Job`', as_dict=True)
	# frappe.db.sql('delete from `tabPortal Job`')
	# for j in jobs:
	# 	if not frappe.db.exists('Country', j.country):
	# 		frappe.get_doc(dict(doctype='Country', country_name=j.country)).insert()
	# 	d = frappe.get_doc(dict(
	# 		doctype='Portal Job',
	# 		title=j.job_title,
	# 		company_name=j.company_name,
	# 		country=j.country,
	# 		status='Open' if j.status=='Assigned' else j.status,
	# 		job_type={
	# 			'ERP Implementation': 'Implementation',
	# 			'Core Development': 'Feature Development',
	# 			'Website Development': 'Website Development',
	# 			'Other': 'App Development'
	# 		}.get(j.job_type, None) or j.job_type,
	# 		description= markdown(j.job_detail),
	# 		owner=j.owner,
	# 		creation=j.creation,
	# 		route=j.route,
	# 		show_in_website=j.show_in_website
	# 	)).insert(ignore_if_duplicate=True, ignore_mandatory=True)
	# 	print d.name

	apps = source.sql('select * from `tabFrappe App`', as_dict=True)
	frappe.db.sql('delete from `tabFrappe App`')
	for a in apps:
		d = frappe.get_doc(dict(
			doctype='Frappe App',
			app_name = a.app_name,
			badge = a.badge,
			category = a.category,
			route = a.route,
			url = a.url,
			repository_url = a.repository_url,
			published = 1,
			description = markdown(a.description),
			owner=a.owner,
			creation=a.creation,
		)).insert(ignore_if_duplicate=True, ignore_mandatory=True)
		print d.name