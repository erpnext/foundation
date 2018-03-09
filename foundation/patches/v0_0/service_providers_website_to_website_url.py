import frappe

def execute():
	frappe.db.sql('''
	update `tabService Provider`
	set website_url = website
	''')
