# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.website.website_generator import WebsiteGenerator

class PortalEvent(WebsiteGenerator):
	def validate(self):
		if not self.route:
			self.route = 'events/' + self.scrub(self.event_title)

def get_list_context(context):
	context.title = 'Upcoming Events'
	context.no_breadcrumbs = True
	context.row_template = 'foundation/templates/includes/portal_event.html'
	context.order_by = 'creation desc'
	context.introduction = '<p><a href="/add-event">Add an event</a></p>'
