from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	context.website_sidebar = 'Conference 2017 Sidebar'
	context.no_breadcrumbs = 1
