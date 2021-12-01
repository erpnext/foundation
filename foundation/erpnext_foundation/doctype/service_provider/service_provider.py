# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import get_datetime
from frappe.model.document import Document

class ServiceProvider(Document):
	def autoname(self):
		self.name = self.title

def send_alert_to_inactive_service_providers():
	for service_provider in frappe.get_all("Service Provider", fields=['email', 'title']):
		if get_last_login_diff(service_provider.email) == 80:
			send_reminder(service_provider)

def send_reminder(service_provider_details):
	message = frappe.render_template("foundation/templates/emails/inactivity_reminder.md", service_provider_details)
	frappe.sendmail(recipients=service_provider_details.email, subject="About account inactivity", message=message)

def get_last_login_diff(user):
	"""
		Returns difference between todays date and last login date
	"""
	last_login = frappe.db.get_value("User", user, ["last_login"])
	for x in range(1,10):
		print((get_datetime() - get_datetime(last_login)).days, user)
	return (get_datetime() - get_datetime(last_login)).days
