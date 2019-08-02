# -*- coding: utf-8 -*-
# Copyright (c) 2017, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ConferenceParticipant(Document):
	def validate(self):
		self.conference = '2019'
		self.send_ticket_mail()

	def validate_payment(self):
		self.amount = self.full_conference_tickets * (5000 if self.currency == 'INR' else 70)

	def on_payment_authorized(self, status_changed_to=None):
		self.paid = 1
		self.save(ignore_permissions=True)

	def send_ticket_mail(self):
		if self.paid == 1 and self.email:
			message = """Thank you for participating in the ERPNext Conference {0}.
			<br> You can find your ticket attached with this email,
			 for more details about the conference please visit https://erpnext.com/conf/{0}""".format(self.conference)
			email_args = {
				"recipients": [self.email],
				"message": message,
				"subject": 'Your Ticket for ERPNext Conference 2019',
				"attachments": [frappe.attach_print(self.doctype, self.name, file_name=self.name, print_format='Conference Ticket')],
				"reference_doctype": self.doctype,
				"reference_name": self.name
			}
			frappe.sendmail(**email_args)
			self.thank_you_email_sent = 1