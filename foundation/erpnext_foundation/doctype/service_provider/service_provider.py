# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import get_datetime

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
		if context.website and not context.website.startswith('http'):
			context.website = 'http://' + context.website


def send_alert_to_inactive_service_providers():
	for service_provider in frappe.get_all("Service Provider", fields=['email', 'title']):
		if get_last_login_diff(service_provider.email) == 80:
			send_reminder(service_provider)

def send_reminder(service_provider_details):
	message = frappe.render_template("foundation/templates/emails/inactivity_reminder.md", service_provider_details)
	frappe.sendmail(recipients=service_provider_details.email, subject="About account inactivity", message=message)

def unpublish_service_provider():
	for service_provider in frappe.get_all("Service Provider", fields=['name', 'title']):
		if get_last_login_diff(service_provider.email) == 90:
			frappe.db.set_value('Service Provider', service_provider.name, 'show_in_website', 0, update_modified=False)


def get_last_login_diff(user):
	"""
		Returns difference between todays date and last login date
	"""
	last_login = frappe.db.get_value("User", user, ["last_login"])
	return (get_datetime() - get_datetime(last_login)).days