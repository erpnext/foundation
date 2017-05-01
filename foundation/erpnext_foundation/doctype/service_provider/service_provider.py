# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class ServiceProvider(WebsiteGenerator):
	_website = frappe._dict(
		condition_field = "show_in_website",
	)
	def validate(self):
		if not self.route:
			self.route = 'service-providers/' + self.scrub(self.name)

	def get_context(self, context):
		context.parents = [dict(label='All Service Providers in {0}'.format(self.country),
			route='service-providers?country={0}'.format(self.country),
			title='All Service Providers in {0}'.format(self.country))]
		if self.member:
			context.membership_type = frappe.get_value('Member', self.member, 'membership_type')
		if not context.website.startswith('http'):
			context.website = 'http://' + context.website