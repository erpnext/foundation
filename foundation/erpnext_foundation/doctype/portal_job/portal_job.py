# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
import foundation

class PortalJob(WebsiteGenerator):
	def get_context(self, context):
		context.parents = [dict(label='View All Jobs',
			route='jobs')]
		context.is_member = foundation.is_member()

	def validate(self):
		if not self.route:
			self.route = 'jobs/' + self.scrub(self.title)

def get_list_context(context):
	context.allow_guest = True
	context.title = 'ERPNext Jobs'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for ERPNext Service Providers</div><br><button class="button green-btn">Post A Job</button>'
