import frappe

def execute():
	frappe.reload_doc("erpnext_foundation", "doctype", "service_provider")
	frappe.db.sql('''
	update `tabService Provider`
	set website_url = website
	''')
