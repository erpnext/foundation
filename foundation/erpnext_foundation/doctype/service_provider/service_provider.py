# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class ServiceProvider(WebsiteGenerator):
	_website = frappe._dict(
		condition_field = "show_in_website",
		template = "templates/generators/service_provider.html"
	)
	def validate(self):
		if not self.route:
			self.route = 'service-providers/' + self.scrub(self.name)

	def get_context(self, context):
		if not context.website.startswith('http'):
			context.website = 'http://' + context.website