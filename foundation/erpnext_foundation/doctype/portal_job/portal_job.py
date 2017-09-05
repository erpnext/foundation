# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.utils import get_fullname, get_link_to_form
import frappe
from frappe import _
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
		if not self.title:
			frappe.throw(_("Job Title is Mandatory for posting a job"))


	def on_update(self):
		service_providers = frappe.get_all('Service Provider', fields=['name', 'email', 'route'])
		sender_fullname = get_fullname(frappe.session.user)
		subject = _("New Job Posted by {0}").format(sender_fullname)
		recipients = [d.email for d in service_providers]

		message = """
			<h2>{title}</h2>
			<table border=1 cellpadding=0 cellspacing=0 style="width: 350px; border-collapse: collapse;">
				<tr>
					<td style="width: 100px; border: 1px solid #dadada; padding: 5px 10px;">Company Name</td>
					<td style="border: 1px solid #dadada; padding: 5px 10px;"> {company_name} </td>
				</tr>
				<tr>
					<td style="border: 1px solid #dadada; padding: 5px 10px;">Country</td>
					<td style="border: 1px solid #dadada; padding: 5px 10px;"> {country}</td>
				</tr>
				<tr>
					<td style="border: 1px solid #dadada; padding: 5px 10px;">Job Type</td>
					<td style="border: 1px solid #dadada; padding: 5px 10px;">{job_type}</td>
				</tr>
			</table>
			<h3>{details}</h3>
			<p>{description}</p>
			<h3>{contact_details}</h3>
			<table border=0 cellpadding=0 cellspacing=0 style="border-collapse: collapse; width: 350px;">
				<tr>
					<td style="width: 100px; border: 1px solid #dadada; padding: 5px 10px;">Contact Name</td>
					<td style="border: 1px solid #dadada; padding: 5px 10px;">{contact_name}</td>
				</tr>
				<tr>
					<td style="border: 1px solid #dadada; padding: 5px 10px;">Contact Number</td>
					<td style="border: 1px solid #dadada; padding: 5px 10px;">{contact_number}</td>
				</tr>
			</table>
			<p><a href="{url}">{view_job}</a></p>
			<p style="font-style:italic;paddng-top:20px;">{note_msg}</p>
			<p>&nbsp;</p>


		""".format(title=self.title, company_name= self.company_name, country=self.country, job_type=self.job_type, details="Details", description= self.description, contact_details="Contact Details", contact_name=sender_fullname, contact_number=self.contact_number, url=self.route, view_job="View this Job Online", note_msg="Note: You are getting this job notification, because you are a member of ERPNext Foundation.")
		frappe.sendmail(recipients = recipients,
				message = message,
				subject = subject)

def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'ERPNext Jobs'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for ERPNext Service Providers</div><br><a class="btn btn-primary" href="/my-jobs?new=1">Post A Job</a>'
