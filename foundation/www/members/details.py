import frappe

def get_context(context):
	if frappe.session.user != 'Guest':
		context.show_sidebar = True
		context.last_membership = frappe.get_all('Membership', 'name,to_date,membership_type',
			dict(member=frappe.session.user), order_by='to_date desc', limit=1)
