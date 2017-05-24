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
		message += '<table border=1 cellpadding=0 cellspacing=0 style="width: 350px; border-collapse: collapse;"><tr><td style="width: 100px; border: 1px solid #dadada; padding: 5px 10px;">Company Name</td><td style="border: 1px solid #dadada; padding: 5px 10px;">' + self.company_name + '</td></tr>'
		message += '<tr><td style="border: 1px solid #dadada; padding: 5px 10px;">Country</td><td style="border: 1px solid #dadada; padding: 5px 10px;">' + self.country + '</td></tr>'
		message += '<tr><td style="border: 1px solid #dadada; padding: 5px 10px;">Job Type</td><td style="border: 1px solid #dadada; padding: 5px 10px;">' + self.job_type + '</td></tr></table>'
		message += '<h3>Details</h3>'
		message += '<p>'+ self.description +'</p>'
		message += '<table border=0 cellpadding=0 cellspacing=0 style="border-collapse: collapse; width: 350px;"><tr><td style="width: 100px; border: 1px solid #dadada; padding: 5px 10px;">Contact Name</td><td style="border: 1px solid #dadada; padding: 5px 10px;">' + frappe.session.user + '</td></tr>'
		message += '<tr><td style="border: 1px solid #dadada; padding: 5px 10px;">Contact Number</td><td style="border: 1px solid #dadada; padding: 5px 10px;">' + self.contact_number + '</td></tr></table>'
		message += '<p><a href="'+ self.route +'">View this Job Online</a></p>'
		message += '<p style="font-style:italic;paddng-top:20px;">Note: You are getting this job notification, because you are a gold/silver/individual member in the ERPNext Foundation.</p>'
		frappe.sendmail(recipients = recipients,
				message = message,
				subject = "New job posted")

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Jobs'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for ERPNext Service Providers</div><br><a class="green-btn" href="/my-jobs?new=1">Post A Job</a>'
