# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.utils import get_fullname, get_link_to_form
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
		service_providers = frappe.get_all('Service Provider', fields=['name', 'email', 'route'])
		sender_fullname = get_fullname(frappe.session.user)
		subject = _("New Job Posted by {0}").format(sender_fullname)
		recipients = [d.email for d in service_providers]
		message = _("""<h2> {0} </h2>"""\
			.format(self.title))
		message += _("""<table border=1 cellpadding=0 cellspacing=0 style="width: 350px; border-collapse: collapse;"><tr><td style="width: 100px; border: 1px solid #dadada; padding: 5px 10px;">Company Name</td><td style="border: 1px solid #dadada; padding: 5px 10px;"> {0} </td></tr>"""\
			.format(self.company_name))
		message += _("""<tr><td style="border: 1px solid #dadada; padding: 5px 10px;">Country</td><td style="border: 1px solid #dadada; padding: 5px 10px;"> {0}</td></tr>"""\
			.format(self.country))
		message += _("""<tr><td style="border: 1px solid #dadada; padding: 5px 10px;">Job Type</td><td style="border: 1px solid #dadada; padding: 5px 10px;">{0}</td></tr></table>"""\
			.format(self.job_type))
		message += '<h3>Details</h3>'
		message += _("""<p>{0}</p>"""\
			.format(self.description))
		message += _("""<table border=0 cellpadding=0 cellspacing=0 style="border-collapse: collapse; width: 350px;"><tr><td style="width: 100px; border: 1px solid #dadada; padding: 5px 10px;">Contact Name</td><td style="border: 1px solid #dadada; padding: 5px 10px;">{0}</td></tr>"""\
			.format(frappe.session.user))
		message += _("""<tr><td style="border: 1px solid #dadada; padding: 5px 10px;">Contact Number</td><td style="border: 1px solid #dadada; padding: 5px 10px;">{0}</td></tr></table>"""\
			.format(self.contact_number))
		message += _("""<p><a href="{0}">View this Job Online</a></p>"""\
			.format(self.route))
		message += '<p style="font-style:italic;paddng-top:20px;">' + frappe._("Note: You are getting this job notification, because you are a gold/silver/individual member in the ERPNext Foundation.")+'</p>'
		message +="<p>&nbsp;</p>"
		frappe.sendmail(recipients = recipients,
				message = message,
				subject = subject)

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Jobs'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for ERPNext Service Providers</div><br><a class="green-btn" href="/my-jobs?new=1">Post A Job</a>'
