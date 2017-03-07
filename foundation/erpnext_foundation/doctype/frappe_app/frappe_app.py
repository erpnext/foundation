# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class FrappeApp(WebsiteGenerator):
	def validate(self):
		if not self.route:
			self.route = 'apps/' + self.scrub(self.app_name)

	def get_context(self, context):
		context.parents = [dict(label='All Apps', route='apps')]


def get_list_context(context):
	context.no_breadcrumbs = True
	context.title = 'Apps / Extensions for ERPNext'