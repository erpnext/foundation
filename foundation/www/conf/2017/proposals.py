import frappe
import frappe.www.list

def get_context(context):
	context.update(frappe.www.list.get_context(context,
		doctype='Conference Talk Proposal'))
