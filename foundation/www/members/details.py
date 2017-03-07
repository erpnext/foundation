import frappe
import foundation

def get_context(context):
	if frappe.session.user != 'Guest':
		context.show_sidebar = True
		context.last_membership = foundation.get_last_membership()
