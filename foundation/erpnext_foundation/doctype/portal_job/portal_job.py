# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
import foundation
from frappe import _


class PortalJob(WebsiteGenerator):
	def get_context(self, context):
		context.no_cache = True
		context.parents = [dict(label='View All Jobs',
			route='erpnext-jobs', title='View All Jobs')]
		context.is_member = foundation.is_member()

	def validate(self):
		if not self.route:
			self.route = 'erpnext-jobs/' + self.scrub(self.title)

	def on_update(self):
		service_provider = frappe.get_all('Service Provider', fields=['name', 'email', 'route'])
		recipients = [d.email for d in service_provider]
		message = '<h2>'+ self.title + '</h2>'
		message += '<table width=300 border=1 cellpadding=0 cellspacing=0><tr><td">Company Name</td><td">' + self.company_name + '</td></tr>'
		message += '<tr><td">Country</td><td">' + self.country + '</td></tr>'
		message += '<tr><td">Job Type</td><td">' + self.job_type + '</td></tr></table>'
		message += '<h3>Details</h3>'
		message += '<p>'+ self.description +'</p>'
		message += '<p><a href="'+ self.route +'">View all jobs</a></p>'
		print recipients
		frappe.sendmail(recipients = service_provider[0].email,
				message = message,
				subject = "New job posted")

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Jobs'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for ERPNext Service Providers</div><br><a class="green-btn" href="/my-jobs?new=1">Post A Job</a>'
