from __future__ import unicode_literals

import frappe
import datetime
from frappe.utils import fmt_money

def get_context(context):
	pass

def get_list_context(context):
	context.row_template = 'erpnext_foundation/doctype/membership/templates/membership_list.html'
	context.get_list = get_site_list

def get_site_list(doctype, txt, filters, limit_start, limit_page_length=20, order_by=None):
	memberships = frappe.db.sql("""select * from `tabMembership`
		where member = %s order by creation desc""", frappe.session.user, as_dict=True)

	for membership in memberships:
		membership.amount = fmt_money(membership.amount, precision=2, currency=membership.currency)

	return memberships