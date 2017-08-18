from __future__ import unicode_literals

import frappe

def get_context(context):
	print(context)
	context.no_breadcrumbs = 1
	context.user = 'faris@erpnext.com'
