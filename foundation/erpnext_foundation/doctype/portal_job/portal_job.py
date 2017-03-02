# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class PortalJob(WebsiteGenerator):
	_website = dict(
		condition_field = "show_in_website",
		template = "templates/generators/portal_job.html"
	)
	def validate(self):
		if not self.route:
			self.route = 'jobs/' + self.scrub(self.title)

def get_list_context(context):
	context.title = 'ERPNext Jobs'
	context.no_breadcrumbs = True
	context.row_template = 'foundation/templates/includes/portal_job.html'
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for ERPNext Service Providers</div><br><button class="button green-btn">Post A Job</button>'
